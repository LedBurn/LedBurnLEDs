#!/usr/bin/env python

import sys, os
sys.path.append(os.path.abspath('../Network'))
import LedBurnProtocol as network
import time

sys.path.append(os.path.abspath('../UIElements'))
from Flower import Flower

flower = Flower()

from ExplosionFlowerAnimation import ExplosionFlowerAnimation
from RainbowFlowerAnimation import RainbowFlowerAnimation
from AlternateFlowerAnimation import AlternateFlowerAnimation
from RoundRobinFlowerAnimation import RoundRobinFlowerAnimation
from NaturalFlowerAnimation import NaturalFlowerAnimation
from FireFlowerAnimation import FireFlowerAnimation
from ConfettiFlowerAnimation import ConfettiFlowerAnimation

props = {'only_top' : False,
		'leds_percent_per_beat' : 0.5,
		'brightness': 0.7}
animation = ConfettiFlowerAnimation(flower, props)

grass 	= [0, 0, 0] * 600
sheep 	= [0, 0 ,0] * 302
sign 	= [0, 0, 0] * 150
lake 	= [0, 0, 0] * 1800

speed = 40 # in 50 hrz
current_time = 0
frame_id = 0;
    
while True:
        
	time_precent = float(current_time) / speed

	animation.apply(time_precent)

	network.send(frame_id, flower.get_array(), sheep, grass, sign, lake)

	time.sleep(0.02)
	current_time = (current_time + 1) % speed
 	frame_id += 1


