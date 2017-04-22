#include <OctoWS2811.h>

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

#define MAX_PACKET_SIZE (8)

#define MAX_PIXELS 600
#define LEDS_PER_STRIP (MAX_PIXELS + 1)
DMAMEM int displayMemory[LEDS_PER_STRIP*6];
int drawingMemory[LEDS_PER_STRIP*6];

const int config = WS2811_GRB | WS2811_800kHz;
OctoWS2811 leds(LEDS_PER_STRIP, displayMemory, drawingMemory, config);

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0x65, 0x65 //last byte should be the hex of the last byte of the ip address
};
IPAddress ip( 10,0,0,211 );
unsigned int localPort = 2000;      // local port to listen on
// An EthernetUDP instance to let us send and receive packets over UDP
EthernetUDP Udp;


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

void PaintLeds(const uint8_t packetBuf[])
{

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
  //Serial.println(packetSize);

  digitalWrite(bluePin, LOW);
  digitalWrite(redPin, LOW);
  
  if (packetSize > 0) {  

    if(packetSize > MAX_PACKET_SIZE)
    {
      Serial.println(packetSize);
      Serial.print("Error");
      digitalWrite(redPin, HIGH);
      return;      
    }

    Serial.print("fft = ");
    uint8_t tempBuf[MAX_PACKET_SIZE];
    Udp.read((uint8_t *)tempBuf, MAX_PACKET_SIZE);
    for(int i = 0; i < MAX_PACKET_SIZE; i++) {
      Serial.print(tempBuf[i]);
      Serial.print(" ");
    }
    Serial.println();
    
    PaintLeds(tempBuf);
  }
}

