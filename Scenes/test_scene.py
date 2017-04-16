#!/usr/bin/env python

import sys, os
sys.path.append(os.path.abspath('../Network'))
import LedBurnProtocol as network
import time

from operator import itemgetter, attrgetter, methodcaller

sys.path.append(os.path.abspath('../UIElements'))
from Flower import Flower
flower = Flower()
from SmallSheep import SmallSheep
sheep = SmallSheep()
from Grass import Grass
grass = Grass()
from Sign import Sign
sign = Sign()


from FireScene import FireScene
from RoundRobinScene import RoundRobinScene
scene = RoundRobinScene(flower, sheep, grass, sign)


speed = 25 # in 50 hrz
current_time = 0
frame_id = 0;

    
while True:
        
	time_precent = float(current_time) / speed

	scene.apply(time_precent)

	network.send(frame_id, flower.get_array(), sheep.get_array(), grass.get_array(), sign.get_array())

	time.sleep(0.02)
	current_time = (current_time + 1) % speed
 	frame_id += 500


