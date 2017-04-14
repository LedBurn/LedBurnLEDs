#!/usr/bin/env python

import lbproto
import ipdb

def test_strips(lbp):
  led  = 0
  strip = 3
  pixel_id = 0
  while True:
    s = raw_input('[strip %d, led %3d, pixel_id %d]:' % (strip, led, pixel_id))

    if not s:
      led += 1
      if led >= 300:
        strip += 1
        led = 0

    elif s.isdigit():
      led = int(s)                                                                                                                                                       
    elif s and s[0] == '+':
      if s[1] == 's':
        strip = int(s[2])
        led = 0
      if s[1] == 'p':
        pixel_id = int(s.split(' ')[1])
        led = 0
  
    leds = [0] * 300 * 3
    leds[3*led + 0] = 255
    leds[3*led + 1] = 255
    leds[3*led + 2] = 255

    lbp.send_simple(strip, leds, pixel_id=pixel_id, debug=False)



lbp = lbproto.LBProtocol('10.0.0.210')

test_strips(lbp)

