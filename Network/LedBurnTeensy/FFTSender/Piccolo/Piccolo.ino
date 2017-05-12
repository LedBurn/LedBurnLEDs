#include <avr/pgmspace.h>
#include "ffft.h"
#include <math.h>
#include <Wire.h>

#ifdef __AVR_ATmega32U4__
#define ADC_CHANNEL 7
#else
#define ADC_CHANNEL 0
#endif

#include <SPI.h>
#include <Ethernet.h>
#include <EthernetUdp.h>

int16_t       capture[FFT_N];       // Audio capture buffer
complex_t     bfly_buff[FFT_N];     // FFT "butterfly" buffer
uint16_t      spectrum[FFT_N / 2];  // Spectrum output buffer
volatile byte samplePos = 0;        // Buffer position counter

#define HISTORY 5
byte
c_level[8],
        peak[8],      // Peak level of each column; used for falling dots
        dotCount = 0, // Frame counter for delaying dot-falling speed
        colCount = 0; // Frame counter for storing past column data
int col[8][HISTORY];   // Column levels for the prior 10 frames
int minLvlAvg[8]; // For dynamic adjustment of low & high ends of graph,
int maxLvlAvg[8]; // pseudo rolling averages for the prior few frames.
int colDiv[8];    // Used when filtering FFT output to 8 columns
int prevSumLevels = 0;

static const uint8_t PROGMEM

col0data[] = {  2,  1, 255,   185 },
             col1data[] = {  2,  0,  // 4 bins, starting at index 1
                             1, 100, 100, 100
                          }, // Weights for 4 bins.  Got it now?
                          col2data[] = {  5,  2,
                                          11, 156, 118,  16,   1
                                       },
                                       col3data[] = {  8,  3,
                                                       5,  55, 165, 164,  71,  18,   4,   1
                                                    },
                                           col4data[] = { 11,  5,
                                                          3,  24,  89, 169, 178, 118,  54,  20,   6,   2,   1
                                                        },
                                               col5data[] = { 17,  7,
                                                              2,   9,  29,  70, 125, 172, 185, 162, 118, 74,
                                                              41,  21,  10,   5,   2,   1,   1
                                                            },
                                                   col6data[] = { 25, 11,
                                                                  1,   4,  11,  25,  49,  83, 121, 156, 180, 185,
                                                                  174, 149, 118,  87,  60,  40,  25,  16,  10,   6,
                                                                  4,   2,   1,   1,   1
                                                                },
                                                       col7data[] = { 37, 16,
                                                                      1,   2,   5,  10,  18,  30,  46,  67,  92, 118,
                                                                      143, 164, 179, 185, 184, 174, 158, 139, 118,  97,
                                                                      77,  60,  45,  34,  25,  18,  13,   9,   7,   5,
                                                                      3,   2,   2,   1,   1,   1,   1
                                                                    },


                                                           // And then this points to the start of the data for each of the columns:
* const colData[]  = {
  col0data, col1data, col2data, col3data,
  col4data, col5data, col6data, col7data
};


/////////// Ethernet ////////////
byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0x64, 0x64
};
IPAddress ip(10, 0, 0, 100);

unsigned int localPort = 8888;      // local port to listen on
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];  //buffer to hold the packet,

// An EthernetUDP instance to let us send and receive packets over UDP
EthernetUDP Udp;
///////////////////////////////

IPAddress destinationIp(10, 0, 0, 211);
unsigned int destinationlPort = 2000;

unsigned long last_sent_time = 0;

void setup() {
  uint8_t i, j, nBins, binNum, *data;

  memset(peak, 0, sizeof(peak));
  memset(col , 0, sizeof(col));

  for (i = 0; i < 8; i++) {
    minLvlAvg[i] = 0;
    maxLvlAvg[i] = 512;
    data         = (uint8_t *)pgm_read_word(&colData[i]);
    nBins        = pgm_read_byte(&data[0]) + 2;
    binNum       = pgm_read_byte(&data[1]);
    for (colDiv[i] = 0, j = 2; j < nBins; j++)
      colDiv[i] += pgm_read_byte(&data[j]);
  }

  // Init ADC free-run mode; f = ( 16MHz/prescaler ) / 13 cycles/conversion
  ADMUX  = ADC_CHANNEL; // Channel sel, right-adj, use AREF pin
  ADCSRA = _BV(ADEN)  | // ADC enable
           _BV(ADSC)  | // ADC start
           _BV(ADATE) | // Auto trigger
           _BV(ADIE)  | // Interrupt enable
           _BV(ADPS2) | _BV(ADPS1) | _BV(ADPS0); // 128:1 / 13 = 9615 Hz
  ADCSRB = 0;                // Free run mode, no high MUX bit
  DIDR0  = 1 << ADC_CHANNEL; // Turn off digital input for ADC pin
  //OCR0A = 0xAF;            // use the same timer as the millis() function
//  TIMSK0 |= _BV(OCIE0A);

  // start the Ethernet and UDP:
  Ethernet.begin(mac, ip);
  Udp.begin(localPort);

  Serial.begin(9600);      // open the serial port at 9600 bps:
  sei(); // Enable interrupts


  Serial.print("Millis: ");
  Serial.println(millis());
}



void loop() {
  Serial.println("before");
  Serial.println(millis());
  Serial.println("after");

  uint8_t  i, x, L, *data, nBins, binNum, weighting, c;
  uint16_t minLvl, maxLvl;
  int      level, y, sum;

  while (ADCSRA & _BV(ADIE)); // Wait for audio sampling to finish
  //  seed=seed+seedInc;

  //  if(seed==maxSeed) seedInc=seedInc*-1;
  //  if(seed==1) seedInc=seedInc*-1;

  fft_input(capture, bfly_buff);   // Samples -> complex #s
  samplePos = 0;                   // Reset sample counter
  ADCSRA |= _BV(ADIE);             // Resume sampling interrupt
  fft_execute(bfly_buff);          // Process complex data
  fft_output(bfly_buff, spectrum); // Complex -> spectrum

  // Remove noise and apply EQ levels
  //  for(x=0; x<FFT_N/2; x++) {
  //    L = pgm_read_byte(&noise[x]);
  //    spectrum[x] = (spectrum[x] <= L) ? 0 :
  //      (((spectrum[x] - L) * (256L - pgm_read_byte(&eq[x]))) >> 8);
  //    Serial.print(spectrum[x]);
  //     Serial.print(" ");
  //  }


  for (x = 0; x < FFT_N / 2; x++) {
    Serial.print(spectrum[x]);
    Serial.print(" ");
  }

  // Downsample spectrum output to 8 columns:
  for (x = 0; x < 8; x++) {

    data   = (uint8_t *)pgm_read_word(&colData[x]);
    nBins  = pgm_read_byte(&data[0]) + 2;
    binNum = pgm_read_byte(&data[1]);
    for (sum = 0, i = 2; i < nBins; i++)
      sum += spectrum[binNum++]; //* pgm_read_byte(&data[i]); // Weighted

    sum = sum / nBins;
    if (sum > 255) {
      sum = 255;
    }

    c_level[x] = sum;

    //    col[x][colCount] = sum / colDiv[x];                    // Average
    //    minLvl = maxLvl = col[x][0];
    //    for (i = 1; i < HISTORY; i++) { // Get range of prior 10 frames
    //      if (col[x][i] < minLvl)      minLvl = col[x][i];
    //      else if (col[x][i] > maxLvl) maxLvl = col[x][i];
    //    }
    //    // minLvl and maxLvl indicate the extents of the FFT output, used
    //    // for vertically scaling the output graph (so it looks interesting
    //    // regardless of volume level).  If they're too close together though
    //    // (e.g. at very low volume levels) the graph becomes super coarse
    //    // and 'jumpy'...so keep some minimum distance between them (this
    //    // also lets the graph go to zero when no sound is playing):
    //    if ((maxLvl - minLvl) < 8) maxLvl = minLvl + 8;
    //    minLvlAvg[x] = (minLvlAvg[x] * 7 + minLvl) >> 3; // Dampen min/max levels
    //    maxLvlAvg[x] = (maxLvlAvg[x] * 7 + maxLvl) >> 3; // (fake rolling average)
    //
    //    // Second fixed-point scale based on dynamic min/max levels:
    //    level = 8L * (col[x][colCount] - minLvlAvg[x]) /
    //            (long)(maxLvlAvg[x] - minLvlAvg[x]);
    //
    //    // Clip output and convert to byte:
    //    if (level < 0L)      c = 0;
    //    else if (level > 8) c = 8; // Allow dot to go a couple pixels off top
    //    else                c = (uint8_t)level;
    //    if(c > peak[x]) peak[x] = c; // Keep dot on top
    //    c = peak[x];
    //    c_level[x] = c;
    //
    //    int sumLevels=0;
    //    for (int i=0;i<8;i++) {
    //        sumLevels+=c_level[i];
    //    }
    //    if(sumLevels==0 && prevSumLevels>0) {
    //        seedInc*=-1;
    //        seed=(seed+(maxSeed/2))%maxSeed;
    //    }
    //    prevSumLevels=sumLevels;
  }

  for (int i = 0; i < 8; i++) {
    Serial.print(c_level[i]);
    Serial.print(" ");
  }


  // send the fft
  Serial.print("Sending - ");
  Udp.beginPacket(destinationIp, destinationlPort);

  //  Udp.write(c_level, 8);
  Udp.write("1234567812345678");
  int sent = Udp.endPacket();
  if (sent == 1)
    Serial.println(" - Sent");
  else
    Serial.println(" - Error");

  // Every third frame, make the peak pixels drop by 1:
  //  if (++dotCount >= 3) {
  //    dotCount = 0;
  //    for (x = 0; x < 8; x++) {
  //      if (peak[x] > 0) peak[x] /= 4;
  //    }
  //  }

  if (++colCount >= HISTORY) colCount = 0;
}

int ticks = 0;
ISR(ADC_vect) { // Audio-sampling interrupt
  ticks++;
  if (ticks >= 1000) {
    ticks = 0;
    static const int16_t noiseThreshold = 0;
    int16_t              sample         = ADC; // 0-1023

    capture[samplePos] =
      ((sample > (512 - noiseThreshold)) &&
       (sample < (512 + noiseThreshold))) ? 0 :
      sample - 512; // Sign-convert for FFT; -512 to +511

    if (++samplePos >= FFT_N) ADCSRA &= ~_BV(ADIE); // Buffer full, interrupt off
  }
}
