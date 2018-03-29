#!/usr/bin/env python

import sys, os
sys.path.append(os.path.abspath('../'))
import Network.LedBurnProtocol as network
import time

from UIElements.Flower import Flower

flower = Flower()

from ExplosionFlowerAnimation import ExplosionFlowerAnimation
from RainbowFlowerAnimation import RainbowFlowerAnimation
from AlternateFlowerAnimation import AlternateFlowerAnimation
from RoundRobinFlowerAnimation import RoundRobinFlowerAnimation
from NaturalFlowerAnimation import NaturalFlowerAnimation
from FireFlowerAnimation import FireFlowerAnimation
from ConfettiFlowerAnimation import ConfettiFlowerAnimation
from GlowFlowerAnimation import GlowFlowerAnimation
from SpikesFlowerAnimation import SpikesFlowerAnimation

# props = {'only_top' : False,
# 		'leds_percent_per_beat' : 0.5,
# 		'brightness': 0.7}
# animation = ConfettiFlowerAnimation(flower, props)
#animation = SpikesFlowerAnimation(flower, {'color':{'type':'const_color', 'hue':0.5}})
animation = ExplosionFlowerAnimation(flower, None)

speed = 200 # in 50 hrz
current_time = 0
frame_id = 0;
    
while True:
        
	time_precent = float(current_time) / speed

	animation.apply(time_precent)

	network.send(flower_data=flower.get_array())

	time.sleep(0.02)
	current_time = (current_time + 1) % speed
 	frame_id += 1


