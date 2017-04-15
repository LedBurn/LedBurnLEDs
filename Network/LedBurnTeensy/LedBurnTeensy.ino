#include <SPI.h>         // needed for Arduino versions later than 0018
#include <Ethernet.h>
#include <EthernetUdp.h>         // UDP library from: bjoern@cs.stanford.edu 12/30/2008

#include <OctoWS2811.h>

// the LedBurn protocol is designed to transfer addressable leds colors data between sender and receiver.
// it is a network protocol, for one way communication between a sender software that generates a scene,
// to a controler software that receives the colors and send them to the pysical leds for display.
// the protocol is aimed to maximize the following properties:
// 1. no configuration or changes to the software in the reciver side.
// 2. support non-reliable network communication.
// 3. minimum latency between frame generation and leds display time.
// 4. avoid displaying leds from different frames where possible.
// 5. support various network setups with differnt MTUs.
// 
// the protocol has a header and payload.
// the header is used to identify the protocol, the current frame, and the current segment.
// header consist of 3 parts:
//
// 1. prtocol definition. 8 byets.
//    1.1 7 charateres in ascii: "LedBurn", used to identify the protocol 
//        and enable the receiver to throw away other packets which might be sent on the port by mistake.
//        also useful to quickly identify the packets when packet sniffing the network for debug.
//    1.2 1 byte of protocol version. current value is 0.
//
// 2. frame definition. 8 bytes containing two uint32 numbers.
//    2.1 first 4 bytes number is the frame id.
//        frame id is serial (advance by one between frames).
//        used to group related segments into a single and synchronized update to the pyhisical leds.
//        overflowing the 32 bits number so it will start with zero again is ok.
//        for 50 frames per seconds, that would happen after 994 days. so in practice it is not expected.
//    2.2 second number is the total number of segments in this frame.
//        used to help the receiver understand that all the segmnets in the frame arrived, 
//        and that frame data is completed.
//
// 3. segment definition. 8 bytes, containes segment id, and first pixel id.
//    3.1 first 4 bytes are the current segment id in the frame.
//        the segment id must be numbered 0...n-1, where n is the total number of segments
//        in the frame, as pusbliesd in 2.2
//    3.2 next 2 byte is the pyisical strip number (should by 0-7 in teensy)
//    3.3 next 2 bytes are the first pixel id in the strip.
//        the amount of pixels in the frame is set by the payload length.
//
// the payload should consist of 3*n bytes, representing n pixels.
// each 3-bytes-pixel should contain the 3 channels for that pixel, as RGB.
// different led-chips may have differrent color order for the red-green-blue tuple.
// correcting the color order should be done on the sender side.
// the recevier is unaware of the actual leds connected to it.
//
// the amount of leds in the payload is not limited by any hard value.
// the sender is able to divide each strip to as many segments as needed.
// 

#define MAX_PIXELS 600
#define LB_HEADER_SIZE (8+8+8)
#define MAX_PACKET_SIZE ( LB_HEADER_SIZE + ( 3 * (MAX_PIXELS)))

 // we add one invisible led due to bug found in octows2811
#define LEDS_PER_STRIP (MAX_PIXELS + 1)

DMAMEM int displayMemory[LEDS_PER_STRIP*6];
int drawingMemory[LEDS_PER_STRIP*6];

const int config = WS2811_GRB | WS2811_800kHz;
OctoWS2811 leds(LEDS_PER_STRIP, displayMemory, drawingMemory, config);

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xD2 //last byte should be the hex of the last byte of the ip address
};
IPAddress ip( 10,0,0,210 );
unsigned int localPort = 2000;      // local port to listen on
// An EthernetUDP instance to let us send and receive packets over UDP
EthernetUDP Udp;

uint32_t currentFrame = 0;

// we support up to 512 segments. it means at least 64 per strip, which is 10 pixels per packet.
// this is more than enough
#define MAX_SUPPORTED_SEGMENTS (8 * 64)
bool receivedSegArr[MAX_SUPPORTED_SEGMENTS] = {false};
uint32_t numOfReceivedSegments = 0;

struct PacketHeaderData
{
  uint32_t frameId;
  uint32_t segInFrame;
  uint32_t currSegId;
  uint16_t stripId;
  uint16_t pixelId;
  uint16_t numOfPixels; // this is not actually header data, but it's nice to have it here
};

//////////////////////////////////////////////////////////
////////////// Indication Leds ///////////////////////////

const int redPin = 17;
const int greenPin = 18;
const int bluePin = 19;

void PaintAllLeds(int color, int pin)
{
  digitalWrite(redPin, LOW);
  digitalWrite(greenPin, LOW);
  digitalWrite(bluePin, LOW);

  digitalWrite(pin, HIGH);  

  for(int i=0; i<leds.numPixels(); i++)
    leds.setPixel(i, color);
  leds.show();
}

void InitIndicationLeds()
{
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  digitalWrite(redPin, HIGH);
  digitalWrite(greenPin, HIGH);
  digitalWrite(bluePin, HIGH);

  delay(500);

  PaintAllLeds(leds.color(128, 0, 0), redPin);
  delay(1000);
  PaintAllLeds(leds.color(0, 128, 0), greenPin);
  delay(1000);
  PaintAllLeds(leds.color(0, 0, 128), bluePin);
  delay(1000); 

  // we should leave only the green, as we have power, but no network or error
  PaintAllLeds(leds.color(0, 0, 0), greenPin);
}

//////////////////////////////////////////////////////////

void SendColorsToStrips()
{
  digitalWrite(bluePin, HIGH);
  digitalWrite(redPin, LOW);
  leds.show();
}


bool VerifyPacket(const uint8_t packetBuf[], int packetSize)
{
  if(packetSize < LB_HEADER_SIZE)
    return false;
  if(memcmp(packetBuf, "LedBurn", 7) != 0)
    return false;  
  uint8_t protocolVersion = packetBuf[7];
  if(protocolVersion != 0)
    return false;
  int payloadLength = (packetSize - LB_HEADER_SIZE);
  if( (payloadLength % 3) != 0)
    return false;

  return true;
}

PacketHeaderData ParsePacketHeader(const uint8_t packetBuf[], int packetSize)
{
  PacketHeaderData phd;
  
  phd.frameId = (*((const uint32_t *) (packetBuf + 8) ));
  phd.segInFrame = (*((const uint32_t *) (packetBuf + 12) ));

  phd.currSegId = (*((const uint32_t *) (packetBuf + 16) ));
  phd.stripId = (*((const uint16_t *) (packetBuf + 20) ));
  phd.pixelId = (*((const uint16_t *) (packetBuf + 22) ));

  phd.numOfPixels = (packetSize - LB_HEADER_SIZE) / 3;

  return phd;
}

void PaintLeds(const uint8_t packetBuf[], const PacketHeaderData &phd)
{
  // avoid overrun the allowed buffer
  if(phd.stripId >= 8)
    return;
  if(phd.pixelId >= MAX_PIXELS)
    return;
  int numOfPixels = min(phd.numOfPixels, (uint16_t)(MAX_PIXELS - phd.pixelId) ); // MAX_PIXELS - phd.pixelId > 0

  // we have 3 pointers to follow:
  // 1. the current led index
  // 2. the source of the rgb to copy from
  // 3. the index in the leds array to copy into
  const uint8_t *sourcePointer = (const uint8_t *)packetBuf + LB_HEADER_SIZE;
  uint32_t destLedIndex = (phd.stripId * LEDS_PER_STRIP) + phd.pixelId; // pixel index, not channel index
  
  for(int i=0; i<numOfPixels; i++)
  {
    leds.setPixel(destLedIndex, *(sourcePointer+0), *(sourcePointer+1), *(sourcePointer+2));
    sourcePointer += 3;
    destLedIndex++;
  }
}

void ResetCounter(uint32_t newFrameId)
{
  currentFrame = newFrameId;
  numOfReceivedSegments = 0;
  for(int i=0; i<MAX_SUPPORTED_SEGMENTS; i++)
    receivedSegArr[i] = false;  
}

// return true if packet is ok.
// return false if packet should be ignored
bool BeforePaintLeds(const PacketHeaderData &phd)
{
  if(phd.segInFrame >= MAX_SUPPORTED_SEGMENTS || phd.currSegId >= phd.segInFrame)
    return false;
  
  // this is the common case with no packet losses
  if(phd.frameId == currentFrame)
    return true;
  
  // if the current frame is old. don't use it!
  // do the math with int64, to avoid overflows
  // unless it's very old, in which case, assume the sender restarted and use it
  int64_t diffFromCurrent = (int64_t)phd.frameId - (int64_t)currentFrame;
  if(diffFromCurrent > -500 && diffFromCurrent < 0) // 500 is 10 seconds in 50HZ
    return false;

  // if we are here, then this frame is not what we expected, but it is not frame from udp re-order.
  // so we change our reference point to it!
  ResetCounter(phd.frameId);
  SendColorsToStrips(); // use the leds we already recived
  return true;
}

void AfterPaintLeds(const PacketHeaderData &phd)
{
  if(receivedSegArr[phd.currSegId])
  {
    // we already have this segment. this is a duplicate packet!
    return;
  }

  receivedSegArr[phd.currSegId] = true;
  numOfReceivedSegments++;

  if(numOfReceivedSegments >= phd.segInFrame)
  {
    ResetCounter(phd.frameId + 1);
    SendColorsToStrips();
  }
}

void setup() {

  // start octows2811
  leds.begin();

  // start the Ethernet and UDP:
  Ethernet.begin(mac, ip);
  Udp.begin(localPort);

  Serial.begin(9600);
  Serial.println("hello");

  InitIndicationLeds();
}

void loop() {
  // if there's data available, read a packet
  int packetSize = Udp.parsePacket();

  digitalWrite(bluePin, LOW);
  
  if (packetSize > 0) {  

    if(packetSize > MAX_PACKET_SIZE)
    {
      digitalWrite(redPin, HIGH);
      return;      
    }
    
    uint8_t tempBuf[MAX_PACKET_SIZE];
    Udp.read((uint8_t *)tempBuf, MAX_PACKET_SIZE);

    if(!VerifyPacket(tempBuf, packetSize))
    {
      digitalWrite(redPin, HIGH);
      return;
    }

    PacketHeaderData phd = ParsePacketHeader(tempBuf, packetSize);
    if(!BeforePaintLeds(phd))
    {
      digitalWrite(redPin, HIGH);
      return;
    }
    PaintLeds(tempBuf, phd);
    AfterPaintLeds(phd);  
  }
}

