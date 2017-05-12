#include <SPI.h>
#include <OctoWS2811.h>

extern "C" {
#include "leds_colors.h"
}

#define MAX_PIXELS 600
#define LEDS_PER_STRIP (MAX_PIXELS + 1)
DMAMEM int displayMemory[LEDS_PER_STRIP * 8];
int drawingMemory[LEDS_PER_STRIP * 8];

const int config = WS2811_GRB | WS2811_800kHz;
OctoWS2811 leds(LEDS_PER_STRIP, displayMemory, drawingMemory, config);
float rand_hue = random();

/////////// Analog In ////////////
int sensorPin = A4;   // line in
int sensorValue = 0;  // value of line in (0 - 1023)
int prevValue = 0; 
int dirSw = 1;

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
  Serial.begin(9600);
    // start octows2811
  leds.begin();
    rand_hue = 0.5;
  Serial.printf("rand_hue=%f", rand_hue);

 // InitIndicationLeds();

}

void loop() {
  delay(50);
  sensorValue = analogRead(sensorPin);
  //  Serial.println(sensorValue);
  sensorValue-=10;

  // Initialise Sensor
  if (sensorValue <= 0) {
    sensorValue=1;
  }
 sensorValue=float(log(sensorValue) / log(2))*100;

  Serial.println(sensorValue);




  // STEM BULB -- [90] -> [152]
  // Test the stem up for indexing
  for (int i=90; i<153; i++) {
    if (i%2==1) {
      if (dirSw==1) {
          leds.setPixel(i, leds.color(sensorValue/80,0,prevValue/80));  
      } else {
          leds.setPixel(i, leds.color(0,sensorValue/80,prevValue/80));
      }
    } else {
      if (dirSw==1) {
          leds.setPixel(i, leds.color(0,sensorValue/80,prevValue/80));
      } else {
          leds.setPixel(i, leds.color(sensorValue/80,0,prevValue/80));  
      }
    }
  }




  // Show the looped pixels  
  leds.show();
  if (prevValue==0 && sensorValue>0) dirSw*=-1;
  prevValue=sensorValue;


}

/*
  TEST IF THE PIXEL ARE INDEXED CORRECTLY

  You are looping through 241 pixels, not 244 
  leds.setPixel[] = [0] [1] ... [243] [244]
  Led number         1   2  ...  244   245
*/

/*
  // LOOP PIXELS [0] -> [244]
  // Run through all the pixels
  for (int i=0; i<240; i++) {
    if (i%2==1) {
      if (dirSw==1) {
          leds.setPixel(i, leds.color(sensorValue/80,0,prevValue/80));  
      } else {
          leds.setPixel(i, leds.color(0,sensorValue/80,prevValue/80));
      }
    } else {
      if (dirSw==1) {
          leds.setPixel(i, leds.color(0,sensorValue/80,prevValue/80));
      } else {
          leds.setPixel(i, leds.color(sensorValue/80,0,prevValue/80));  
      }
    }
  }
*/

/*
  // STEM UP First Hundred Pixels [0] -> [89]
  // Test the stem up for indexing
  for (int i=0; i<89; i++) {
    if (i%2==1) {
      if (dirSw==1) {
          leds.setPixel(i, leds.color(sensorValue/80,0,prevValue/80));  
      } else {
          leds.setPixel(i, leds.color(0,sensorValue/80,prevValue/80));
      }
    } else {
      if (dirSw==1) {
          leds.setPixel(i, leds.color(0,sensorValue/80,prevValue/80));
      } else {
          leds.setPixel(i, leds.color(sensorValue/80,0,prevValue/80));  
      }
    }
  }
*/

/*
  // STEM BULB -- [90] -> [152]
  // Test the stem up for indexing
  for (int i=90; i<153; i++) {
    if (i%2==1) {
      if (dirSw==1) {
          leds.setPixel(i, leds.color(sensorValue/80,0,prevValue/80));  
      } else {
          leds.setPixel(i, leds.color(0,sensorValue/80,prevValue/80));
      }
    } else {
      if (dirSw==1) {
          leds.setPixel(i, leds.color(0,sensorValue/80,prevValue/80));
      } else {
          leds.setPixel(i, leds.color(sensorValue/80,0,prevValue/80));  
      }
    }
  }
*/

/*
  // STEM DOWN -- Last Hundred Pixels 100 [153] .. 
  // Test the stem up for indexing
  for (int i=153; i<244; i++) {
    if (i%2==1) {
      if (dirSw==1) {
          leds.setPixel(i, leds.color(sensorValue/80,0,prevValue/80));  
      } else {
          leds.setPixel(i, leds.color(0,sensorValue/80,prevValue/80));
      }
    } else {
      if (dirSw==1) {
          leds.setPixel(i, leds.color(0,sensorValue/80,prevValue/80));
      } else {
          leds.setPixel(i, leds.color(sensorValue/80,0,prevValue/80));  
      }
    }
  }
*/

