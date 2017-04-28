#!/usr/bin/env python

import sys, os
sys.path.append(os.path.abspath('../'))
import time

import Network.LedBurnProtocol as network

from UIElements.Sign import Sign

sign = Sign()

from FireSignAnimation import FireSignAnimation
from HueSignAnimation import HueSignAnimation
from RainbowSignAnimation import RainbowSignAnimation

#animation = HueSignAnimation(sign, {"animated": True, "full_color": True})
animation = RainbowSignAnimation(sign, None)

speed = 50 # in 50 hrz
current_time = 0
frame_id = 0;
    
while True:
        
	time_precent = float(current_time) / speed

	animation.apply(time_precent)

	network.send(frame_id, sign_data=sign.get_array())

	time.sleep(0.05)
	current_time = (current_time + 1) % speed
 	frame_id += 500


