#include <SPI.h>
#include <OctoWS2811.h>

extern "C" {
#include "leds_colors.h"
}

/// Flower 1 :  Stem: 0-89, 150-240
///             Bulb: 90-149

/// Flower 2 :  Stem: 0-119, 180-300
///             Bulb: 120-179

/// Flower 3 :  Stem: 0-119, 180-300
///             Bulb: 120-179

/// Mashroom Small and Tall:
/// 


// Teensy 1:
// 1. 
// 2.
// 3.
// 4.
// 5.
// 6.
// 7.
// 8. Eq

// Teensy 2:
//

#define MAX_PIXELS 600
#define LEDS_PER_STRIP (MAX_PIXELS + 1)
DMAMEM int displayMemory[LEDS_PER_STRIP * 8];
int drawingMemory[LEDS_PER_STRIP * 8];

const int config = WS2811_GRB | WS2811_800kHz;
OctoWS2811 leds(LEDS_PER_STRIP, displayMemory, drawingMemory, config);
float rand_hue = random();

int bulbOffset=120; //flower 1=90, flower 2=120
int bulbLastIndex=179; //flower 1=149, flower 2=179
int lastIndex=300; //flower 1=240, flower 2=300
int sensorPin = 4;   // line in
int sensorValue = 0;  // value of line in (0 - 1023)
int sensorLogValue = 0;  // value of line in (0 - 1023)
int prevValue = 0; 
int prevLogValue = 0; 
int dirSw = 1;
int fps = 25;
int frameCount = 0;
int spinCount=0;
float spinThreshold=0.8;
float quietThreshold=0.05;
int quietCounter;
int r=255, g=0, b=0;
float sensorDecay=0.075;
int idleSpinDegrees=3;
int fastSpinDegrees=30;
int peakLevel=1000;
int prevSensorValue=0;

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
//  PaintAllLeds(leds.color(0, 0, 0), greenPin);
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
  delay(1000/fps);
  frameCount+=1;
  if (frameCount==fps) frameCount=0;
  
  sensorValue = analogRead(sensorPin);

  

  
  //  Serial.println(sensorValue);
//  sensorValue-=15;
//  if (sensorValue <= 0) {
//  sensorValue=0;
//  }

  

  sensorLogValue=float(sqrt(sensorValue))*32;

  if (prevLogValue-sensorLogValue>sensorDecay*peakLevel) {
    sensorLogValue=prevLogValue-(sensorDecay*peakLevel);
    sensorValue=prevValue-(sensorDecay*peakLevel);
  }
//  if (peakLevel<sensorLogValue) peakLevel=sensorLogValue;

  Serial.println(sensorValue);
  Serial.print(", ");
  Serial.println(sensorLogValue);

  for (int i=0; i<9; i++) {
    for (int j=0; j<7; j++) {
        hsv color_hsv;
        color_hsv.h = (spinCount+(i*40))%360;
        color_hsv.s = 1.0;
        color_hsv.v = 0.6;

        rgb rgb_color = hsv2rgb(color_hsv);
  
      //leds.setPixel(i+90+((j*9+spinCount)%54), 25*i*(float(sensorValue/1000)+1),25*((i+3)%9)*(float(sensorValue/1000)+1),25*((i+6)%9)*(float(sensorValue/1000)+1));    
//strip 1
      leds.setPixel(bulbOffset+i+(j*9),int(rgb_color.r * 255),int(rgb_color.g * 255),int(rgb_color.b * 255));
//strip 2
     leds.setPixel(bulbOffset+i+(j*9)+LEDS_PER_STRIP,int(rgb_color.r * 255),int(rgb_color.g * 255),int(rgb_color.b * 255));

    }
  }


  for (int i=0; i<=lastIndex; i++) {
    if (i<bulbOffset || i>bulbLastIndex) {
      if (i<bulbOffset) {
        if (dirSw==1) {
            leds.setPixel(i, leds.color(sensorLogValue/80,0,prevLogValue/80)); 
            leds.setPixel(i+LEDS_PER_STRIP, leds.color(sensorLogValue/80,0,prevLogValue/80));  
        } else {
            leds.setPixel(i, leds.color(0,sensorLogValue/80,prevLogValue/80));
            leds.setPixel(i+LEDS_PER_STRIP, leds.color(0,sensorLogValue/80,prevLogValue/80));
        }
      } else {
        if (dirSw==1) {
            leds.setPixel(i, leds.color(0,sensorLogValue/80,prevLogValue/80));
            leds.setPixel(i+LEDS_PER_STRIP, leds.color(0,sensorLogValue/80,prevLogValue/80));
        } else {
            leds.setPixel(i, leds.color(sensorLogValue/80,0,prevLogValue/80));  
            leds.setPixel(i+LEDS_PER_STRIP, leds.color(sensorLogValue/80,0,prevLogValue/80));  
        }
      }
    }

  }

// strip 1
  for (int i=bulbOffset; i<=bulbOffset+9; i++) {
    leds.setPixel(i, leds.color((sensorLogValue/(spinThreshold*peakLevel))*150,0,0));  
  }
// strip 2
  for (int i=bulbOffset+LEDS_PER_STRIP; i<=bulbOffset+9+LEDS_PER_STRIP; i++) {
    leds.setPixel(i, leds.color((sensorLogValue/(spinThreshold*peakLevel))*150,0,0));  
  }


// strip 8 (meter)
int eqLevel=analogRead(sensorPin)/78;

for (int i=0; i<13; i++) {
  if (i<eqLevel) {
      leds.setPixel(i+LEDS_PER_STRIP*7, leds.color(5,0,50));  
      leds.setPixel(LEDS_PER_STRIP*7+25-i, leds.color(5,0,50));  
  } else {
      leds.setPixel(i+LEDS_PER_STRIP*7, leds.color(0,0,0));   
      leds.setPixel(LEDS_PER_STRIP*7+25-i, leds.color(0,0,0));  
  }

  if (eqLevel==13) {
    leds.setPixel(LEDS_PER_STRIP*7+12, leds.color(50,5,0));  
    leds.setPixel((LEDS_PER_STRIP*7+25)-12, leds.color(50,5,0));  
  }
}

//strips 3-7
for (int i=0; i<10; i++) {
    for (int j=0; j<22; j++) {
        hsv color_hsv;
        color_hsv.h = (spinCount+(i*10))%360;
        color_hsv.s = 1.0;
        color_hsv.v = 0.3;

        rgb rgb_color = hsv2rgb(color_hsv);
      for (int k=3; k<=7; k++) {
              leds.setPixel(LEDS_PER_STRIP*(k-1)+i+(j*20),int(rgb_color.r * 255),int(rgb_color.g * 255),int(rgb_color.b * 255));
      }
    }
  }

  leds.show();

  
  if (prevSensorValue<=peakLevel*quietThreshold){
    if  (sensorLogValue>peakLevel*quietThreshold) {
      dirSw*=-1;
      quietCounter=0;
    }
    else  {
      quietCounter++;
    }
  }

//  if (quietCounter==fps/2) peakLevel=peakLevel*spinThreshold;
  
  if (sensorLogValue>=spinThreshold*peakLevel) {
  
    spinCount=(spinCount+fastSpinDegrees)%360;
  } else {
   spinCount=(spinCount+idleSpinDegrees)%360; 
  }
    if (spinCount==360) spinCount=0;
 // }
  
  prevValue=sensorValue;
  prevLogValue=sensorLogValue;
  prevSensorValue=analogRead(sensorPin);
  
  
}
