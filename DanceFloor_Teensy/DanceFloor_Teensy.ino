#include <OctoWS2811.h>

#define MAX_PIXELS 600
#define LEDS_PER_STRIP (MAX_PIXELS + 1)
DMAMEM int displayMemory[LEDS_PER_STRIP*8];
int drawingMemory[LEDS_PER_STRIP*8];

const int config = WS2811_GRB | WS2811_800kHz;
OctoWS2811 leds(LEDS_PER_STRIP, displayMemory, drawingMemory, config);


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

void setup() {

  // start octows2811
  leds.begin();

  Serial.begin(9600);
  Serial.println("hello");

  InitIndicationLeds();
}

void loop() {
  for(int i=0; i<244; i++) {
    if (i<94) 
      leds.setPixel(i+4*600, 200, 0 ,0);

    else if (i<154) 
      leds.setPixel(i+4*600, 0, 200 ,0);
    
    else
      leds.setPixel(i+4*600, 200, 30 ,30);
  }
  
  leds.show();
  delay(20); 
}

