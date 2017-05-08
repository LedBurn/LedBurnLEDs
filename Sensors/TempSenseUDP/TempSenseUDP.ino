#include <OneWire.h>
#include <DallasTemperature.h>
#include <SPI.h>    // needed for Arduino versions later than 0018
#include <Ethernet.h>
#include <EthernetUdp.h>

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 220 };
IPAddress localIp(10, 0, 0, 220);
//IPAddress serverIp(10, 0, 0, 200);
IPAddress serverIp(255, 255, 255, 255);

unsigned int localPort = 8888;      // local port to listen on

EthernetUDP Udp;

// Data wire is plugged into pin 2 on the Arduino
#define ONE_WIRE_BUS 2
 
// Setup a oneWire instance to communicate with any OneWire devices 
// (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);
 
// Pass our oneWire reference to Dallas Temperature.
DallasTemperature sensors(&oneWire);

float tempRead = 0.0;
String  tempString = "No read";
 
void setup(void)
{
  pinMode(4, OUTPUT);
  digitalWrite(4, HIGH);   // de-select the SD Card
  // start serial port
  Serial.begin(9600);
  Serial.println("Dallas Temperature IC Control Library Demo");

  // Start up the library
  sensors.begin();

  Ethernet.begin(mac,localIp);
  Serial.println(Ethernet.localIP());
  Udp.begin(localPort);  
}
 
 
void loop(void)
{
  // call sensors.requestTemperatures() to issue a global temperature
  // request to all devices on the bus
  Serial.print(" Requesting temperatures...");
  sensors.requestTemperatures(); // Send the command to get temperatures
  Serial.println("DONE");

  Serial.print("Temperature is: ");
  tempRead = sensors.getTempCByIndex(0);
  Serial.print(tempRead); // Why "byIndex"? 
    // You can have more than one IC on the same bus. 
    // 0 refers to the first IC on the wire

  Udp.beginPacket(serverIp, 5005);
  tempString = String(tempRead,2);
  Udp.write(tempString.c_str());

  Udp.endPacket();

  delay(1000);
  
}

