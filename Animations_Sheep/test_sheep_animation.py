#!/usr/bin/env python

import sys, os
sys.path.append(os.path.abspath('../Network'))
import LedBurnProtocol as network
import time

sys.path.append(os.path.abspath('../UIElements'))
from SmallSheep import SmallSheep

sheep = SmallSheep()

from SpikeSheepAnimation import SpikeSheepAnimation
from FireSheepAnimation import FireSheepAnimation
animation = FireSheepAnimation(sheep)

flower 	= [0, 0, 0] * 550
grass 	= [0, 0, 0] * 600
sign 	= [0, 0, 0] * 150
lake 	= [0, 0, 0] * 1800

speed = 100 # in 50 hrz
current_time = 0
frame_id = 0;
    
while True:
        
	time_precent = float(current_time) / speed

	animation.apply(time_precent)

	network.send(frame_id, flower, sheep.get_array(), grass, sign, lake)

	time.sleep(0.02)
	current_time = (current_time + 1) % speed
 	frame_id += 500


