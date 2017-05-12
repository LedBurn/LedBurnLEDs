#include <SPI.h>         // needed for Arduino versions later than 0018
#include <Ethernet.h>
#include <EthernetUdp.h>         // UDP library from: bjoern@cs.stanford.edu 12/30/2008

#include <OctoWS2811.h>

extern "C" {
#include "leds_colors.h"
}

#define MAX_PACKET_SIZE (8)

#define MAX_PIXELS 600
#define LEDS_PER_STRIP (MAX_PIXELS + 1)
DMAMEM int displayMemory[LEDS_PER_STRIP * 8];
int drawingMemory[LEDS_PER_STRIP * 8];

const int config = WS2811_GRB | WS2811_800kHz;
OctoWS2811 leds(LEDS_PER_STRIP, displayMemory, drawingMemory, config);

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0x65, 0x65 //last byte should be the hex of the last byte of the ip address
};
IPAddress ip( 10, 0, 0, 211 );
unsigned int localPort = 2000;      // local port to listen on
// An EthernetUDP instance to let us send and receive packets over UDP
EthernetUDP Udp;

float rand_hue = random();
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];  //buffer to hold incoming packet,

int counter = 0;

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

  for (int i = 0; i < leds.numPixels(); i++)
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
  float average = 0.0;
  for (int i = 0; i < 8; i++) {
    average += packetBuf[i];
  }
  average = average / 8;
  if (average > 255) {
    average = 255.0;
  }

  hsv hsv_color;
  hsv_color.h = rand_hue * 360;
  hsv_color.s = 1.0;
  hsv_color.v = average / 255.0;
  rgb rgb_color = hsv2rgb(hsv_color);


  int color = leds.color((int)(rgb_color.r * 255.0), (int)(rgb_color.g * 255.0), (int)(rgb_color.b * 255.0));
  Serial.println(color);
  for (int i = 0; i < leds.numPixels(); i++) {
    leds.setPixel(i, color);
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

  rand_hue = 0.5;
  Serial.printf("rand_hue=%f", rand_hue);

  InitIndicationLeds();

}

void loop() {
  //  Serial.println("start loop");
  //  // if there's data available, read a packet
  //  int packetSize = Udp.parsePacket();
  //Serial.printf("size = %d", packetSize);
  //
  ////  digitalWrite(bluePin, LOW);
  ////  digitalWrite(redPin, LOW);
  //
  //  if (packetSize > 0) {
  //    if(packetSize > MAX_PACKET_SIZE)
  //    {
  //      Serial.println(packetSize);
  //      Serial.print("Error");
  ////      digitalWrite(redPin, HIGH);
  //      Udp.flush();
  //      Serial.println("flush");
  //    } else {
  //
  //     Serial.print("fft = ");
  //     uint8_t tempBuf[MAX_PACKET_SIZE];
  //      Udp.read((uint8_t *)tempBuf, MAX_PACKET_SIZE);
  //      Udp.flush();
  //      for(int i = 0; i < MAX_PACKET_SIZE; i++) {
  //       Serial.print(tempBuf[i]);
  //       Serial.print(" ");
  //     }
  //     Serial.println();
  //
  ////     digitalWrite(bluePin, HIGH);
  ////     PaintLeds(tempBuf);
  ////     leds.show();
  //
  //    }
  //  }
  //  Serial.flush();
  // if there's data available, read a packet
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    counter++;
    Serial.print("Received packet of size ");
    Serial.println(packetSize);
    Serial.print("From ");
    IPAddress remote = Udp.remoteIP();
    for (int i = 0; i < 4; i++) {
      Serial.print(remote[i], DEC);
      if (i < 3) {
        Serial.print(".");
      }
    }
    Serial.print(", port ");
    Serial.println(Udp.remotePort());

    // read the packet into packetBufffer
    Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
    Serial.println("Contents:");
    Serial.println(packetBuffer);
    Serial.printf("Counter = %d", counter);
  }
  delay(10);
}

