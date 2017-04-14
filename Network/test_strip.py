#!/usr/bin/env python

import lbproto
import ipdb

def test_strips(lbp):
  led  = 0
  strip = 3
  while True:
    s = raw_input('[strip %d, led %3d]:' % (strip, led))

    if not s:
      led += 1
      if led >= 600:
        strip += 1
        led = 0

    elif s.isdigit():
      led = int(s)                                                                                                                                                       
    elif s and s[0] == '+':
      if s[1] == 's':
        strip = int(s[2])
        led = 0
  
    leds = [0] * 150 * 3
    leds[3*led + 0] = 255
    leds[3*led + 1] = 255
    leds[3*led + 2] = 255

    lbp.send_simple(strip, leds, debug=False)



lbp = lbproto.LBProtocol('10.0.0.210')

test_strips(lbp)

