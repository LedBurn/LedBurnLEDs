#include <SPI.h>
#include <Ethernet.h>
#include <EthernetUdp.h>

/////////// Analog In ////////////
int sensorPin = A4;   // line in
int sensorValue = 0;  // value of line in (0 - 1023)


/////////// Ethernet ////////////
//byte mac[] = {0xDE, 0xAD, 0xBE, 0xEF, 0x64, 0x64};
//IPAddress ip(10, 0, 0, 100);
//
//unsigned int localPort = 8888;      // local port to listen on
//char packetBuffer[UDP_TX_PACKET_MAX_SIZE];  //buffer to hold the packet,

// An EthernetUDP instance to let us send and receive packets over UDP
//EthernetUDP Udp;
//
//IPAddress destinationIp(10, 0, 0, 101);
//unsigned int destinationlPort = 5001;

///////////////////////////////


void setup() {
//  Ethernet.begin(mac, ip);
//  Udp.begin(localPort);

  Serial.begin(9600);
}

void loop() {
  delay(20);

  // read analog value
  sensorValue = analogRead(sensorPin);

  // send
//  Serial.print("Sending - ");
  Serial.println(sensorValue);
//  Udp.beginPacket(destinationIp, destinationlPort);
//  Udp.print(sensorValue);
//  int sent = Udp.endPacket();
//  if (sent == 1)
//    Serial.println(" - Sent");
//  else
//    Serial.println(" - Error");
}
