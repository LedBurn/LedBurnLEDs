#include <Ethernet.h>
#include <EthernetUdp.h>

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 221 };
IPAddress localIp(10, 0, 0, 221);
//IPAddress serverIp(10, 0, 0, 200);
IPAddress serverIp(255, 255, 255, 255);

unsigned int localPort = 8888;      // local port to listen on

EthernetUDP Udp;

// Data wire is plugged into pin 2 on the Arduino
#define DATA_PIN 2
 
void setup(void)
{
  // start serial port
  Serial.begin(9600);
  Serial.println("Motion Sensor data sent by UDP program");

  pinMode(DATA_PIN, INPUT);

  Ethernet.begin(mac, localIp);
  Udp.begin(localPort);  
}
 
 
void loop(void)
{
  Serial.print(" Reading motion sensor...");
  int motionState = digitalRead(DATA_PIN);
  Serial.println("DONE");

  Serial.print("Motion state is: ");
  Serial.print(motionState);

  Udp.beginPacket(serverIp, 5006);
  Udp.write(String(motionState).c_str());

  Udp.endPacket();

  delay(1000);
  
}

