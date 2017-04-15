#!/usr/bin/env python

import sys, os
sys.path.append(os.path.abspath('../Network'))
import LedBurnProtocol as network
import time

sys.path.append(os.path.abspath('../UIElements'))
from Flower import Flower

flower = Flower()

from RainbowFlowerAnimation import RainbowFlowerAnimation

animation = RainbowFlowerAnimation(flower)

grass 	= [0, 0, 0] * 600
sheep 	= [0, 0 ,0] * 302
sign 	= [0, 0, 0] * 150

speed = 100 # in 50 hrz
current_time = 0
frame_id = 0;
    
while True:
        
	time_precent = float(current_time) / speed

	animation.apply(time_precent)

	network.send(frame_id, flower.get_array(), sheep, grass, sign)

	time.sleep(0.02)
	current_time = (current_time + 1) % speed
 	frame_id += 500


