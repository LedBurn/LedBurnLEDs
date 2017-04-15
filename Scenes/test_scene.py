#!/usr/bin/env python

import sys, os
sys.path.append(os.path.abspath('../Network'))
import LedBurnProtocol as network
import time

sys.path.append(os.path.abspath('../UIElements'))
from SmallSheep import SmallSheep
sheep = SmallSheep()
from Grass import Grass
grass = Grass()
from Sign import Sign
sign = Sign()

from FireScene import FireScene
scene = FireScene(None, sheep, grass, sign)

flower 	= [0, 0, 0] * 550

speed = 25 # in 50 hrz
current_time = 0
frame_id = 0;
    
while True:
        
	time_precent = float(current_time) / speed

	scene.apply(time_precent)

	network.send(frame_id, flower, sheep.get_array(), grass.get_array(), sign.get_array())

	time.sleep(0.02)
	current_time = (current_time + 1) % speed
 	frame_id += 500


