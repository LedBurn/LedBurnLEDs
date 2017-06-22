#include <SPI.h>
#include <OctoWS2811.h>

typedef struct {
  uint16_t bottom[2];
  uint16_t top[2];
  uint16_t dots[12];
} Mushroom;

typedef struct {
  uint16_t bulbOffset;
//  uint16_t bottom[2];
//  uint16_t top[2];
} Flower;

extern "C" {
#include "leds_colors.h"
}


/// Flower 1 :  Stem: 0-89, 150-240
///             Bulb: 90-149

/// Flower 2 :  Stem: 0-119, 180-300
///             Bulb: 120-179

/// Flower 3 :  Stem: 0-119, 180-300
///             Bulb: 120-179

Mushroom smallAndTallMushroom;
Mushroom smallAndShortMushroom;
Mushroom bigMushroom;

Flower standardFlower;

//m.bottom[0] = 0;
//m.bottom = {0 , 113};
//m.top = {132 , 419};

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

#define SENSOR_PIN 4 // line in
#define FPS 25

int bulbOffset=120; //flower 1=90, flower 2=120
int bulbLastIndex=179; //flower 1=149, flower 2=179
int lastIndex=300; //flower 1=240, flower 2=300

#define SPIN_THRESHOLD 800
#define QUIET_THRESHOLD 5
#define SENSOR_DECAY 75

// Sensor Values;
int prevValue = 0; 
double prevLogValue = 0;
int sensorValue = 0;
double sensorLogValue = 0;

// SPIN DEGREES
double superSlowSpinDegree = 0; // changes 0.2 const
double spinDegree = 0; // changes according to music
uint8_t dirSw = 1;

void initElements() {
  smallAndTallMushroom.bottom[0] = 0;
  smallAndTallMushroom.bottom[1] = 113;
  smallAndTallMushroom.top[0] = 132;
  smallAndTallMushroom.top[1] = 419;

  bigMushroom.bottom[0] = 0;
  bigMushroom.bottom[1] = 139;
  bigMushroom.top[0] = 156;
  bigMushroom.top[1] = 599;

  smallAndShortMushroom.bottom[0] = 0;
  smallAndShortMushroom.bottom[1] = 68;
  smallAndShortMushroom.top[0] = 82;
  smallAndShortMushroom.top[1] = 299;

  standardFlower.bulbOffset = 120;
//  standardFlower.bottom[0] = 0;
//  standardFlower.bottom[1] = 68;
//  standardFlower.top[0] = 82;
//  standardFlower.top[1] = 299;
}

void initIndicationLeds() {
  delay(500);
  paintAllLeds(leds.color(128, 0, 0));
  delay(1000);
  paintAllLeds(leds.color(0, 128, 0));
  delay(1000);
  paintAllLeds(leds.color(0, 0, 128));
  delay(1000);
}

void paintAllLeds(int color) {
  for (int i = 0; i < leds.numPixels(); i++)
    leds.setPixel(i, color);
  leds.show();
}

void paintEq(uint8_t  pin) {
  int eqLevel = sensorValue/78;
  int startingLed = LEDS_PER_STRIP*(pin-1);

  for (int i=0; i<13; i++) {
    if (i<eqLevel) {
        leds.setPixel(startingLed + i, leds.color(5,0,50));  
        leds.setPixel(startingLed + 25 - i, leds.color(5,0,50));  
    } else {
        leds.setPixel(startingLed + i, leds.color(0,0,0));   
        leds.setPixel(startingLed + 25 - i, leds.color(0,0,0));  
    }
  
    if (eqLevel==13) {
      leds.setPixel(startingLed + 12, leds.color(50,5,0));  
      leds.setPixel(startingLed + 13, leds.color(50,5,0));  
    }
  }
}

void paintMushroom(Mushroom *m, uint8_t pin) {
  int startingLed = LEDS_PER_STRIP*(pin-1);

  // calculate color based on the super slow spin
  hsv color_hsv;
  color_hsv.h = superSlowSpinDegree;
  color_hsv.s = 1.0;
  color_hsv.v = 0.3;
  rgb rgb_color = hsv2rgb(color_hsv);

  // paint bottom + top
  for (int i=m->bottom[0]; i<=m->bottom[1]; i++) {
    leds.setPixel(startingLed + i, int(rgb_color.r * 255),int(rgb_color.g * 255),int(rgb_color.b * 255));   
  }
  for (int i=m->top[0]; i<=m->top[1]; i++) {
    leds.setPixel(startingLed + i, int(rgb_color.r * 255),int(rgb_color.g * 255),int(rgb_color.b * 255));   
  }

  // random new dots - if we're in a peak
  if (sensorLogValue >= SPIN_THRESHOLD) {
    for (int i=0; i<12; i++) {
      uint16_t dot = random(m->top[0], m->top[1]+1);
      m->dots[i] = dot;
    }
  }

  // paint dots
  for (int i=0; i<12; i++) {
   leds.setPixel(startingLed + m->dots[i], leds.color(255,255,255));
  }

  // turn off leds
  for (int i=m->bottom[1]+1; i<m->top[0]; i++) {
    leds.setPixel(startingLed + i, leds.color(0,0,0));   
  }
}

void paintFlower(Flower *f, uint8_t pin) {
  int startingLed = LEDS_PER_STRIP*(pin-1);
  int bulbOffset = f->bulbOffset; //flower 1=90, flower 2=120
  
  for (int i=0; i<9; i++) {
    for (int j=0; j<7; j++) {
      double degree = spinDegree + (i * 40);
      while (degree >= 360) degree -= 360;

      hsv color_hsv;
      color_hsv.h = degree;
      color_hsv.s = 1.0;
      color_hsv.v = 0.6;
      
      rgb rgb_color = hsv2rgb(color_hsv);   
      leds.setPixel(startingLed + bulbOffset + i + j*9,int(rgb_color.r * 255),int(rgb_color.g * 255),int(rgb_color.b * 255));
    }
  }
}

void paintSimpleStrip(uint8_t pin) {
  for (int i=0; i<10; i++) {
    double degree = spinDegree + (i * 10);
    while (degree >= 360) degree -= 360;
    
    hsv color_hsv;
    color_hsv.h = degree;
    color_hsv.s = 1.0;
    color_hsv.v = 0.3;
    rgb rgb_color = hsv2rgb(color_hsv);
        
    for (int j=0; j<22; j++) {
        leds.setPixel(LEDS_PER_STRIP*(pin-1)+i+(j*20),int(rgb_color.r * 255),int(rgb_color.g * 255),int(rgb_color.b * 255));
    }
  }
}


void setup() {
  Serial.begin(9600);
  leds.begin();
  initIndicationLeds();
  initElements();
}

void loop() {
  Serial.println("New Loop");
  delay(1000/FPS);

  // calculate the new sensor values
  sensorValue = analogRead(SENSOR_PIN);
  sensorLogValue = sqrt(sensorValue)*32;
  if (prevLogValue - sensorLogValue > SENSOR_DECAY) {
    sensorLogValue = prevLogValue - SENSOR_DECAY;
    sensorValue = prevValue - SENSOR_DECAY;
  }

  // update spin value
    if (sensorLogValue >= SPIN_THRESHOLD) {
    spinDegree += 3;
  } else {
    spinDegree += 30; 
  }
  while (spinDegree >= 360) spinDegree -= 360;

  // update super slow spin value
  superSlowSpinDegree += 0.2;
  while (superSlowSpinDegree >= 360) superSlowSpinDegree -= 360;

  // update direction switch
  if ((prevLogValue <= QUIET_THRESHOLD) && (sensorLogValue > QUIET_THRESHOLD)) { // first noise after quiet
      dirSw *= -1;
  }
  

  for (int i=0; i<9; i++) {
    for (int j=0; j<7; j++) {
      double degree = spinDegree + (i * 40);
      while (degree >= 360) degree -= 360;

      hsv color_hsv;
      color_hsv.h = degree;
      color_hsv.s = 1.0;
      color_hsv.v = 0.6;
      
      rgb rgb_color = hsv2rgb(color_hsv);   
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
    leds.setPixel(i, leds.color((sensorLogValue/(SPIN_THRESHOLD))*150,0,0));  
  }
// strip 2
  for (int i=bulbOffset+LEDS_PER_STRIP; i<=bulbOffset+9+LEDS_PER_STRIP; i++) {
    leds.setPixel(i, leds.color((sensorLogValue/(SPIN_THRESHOLD))*150,0,0));  
  }


  // paint leds
  paintFlower(&standardFlower, 4);
  paintMushroom(&smallAndShortMushroom, 7);
  paintEq(8);
  leds.show();

  // save sensor values
  prevValue=sensorValue;
  prevLogValue=sensorLogValue;
}
