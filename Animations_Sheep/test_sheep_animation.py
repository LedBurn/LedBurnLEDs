#!/usr/bin/env python

import sys, os
sys.path.append(os.path.abspath('../'))
import Network.LedBurnProtocol as network
import time

from UIElements.SmallSheep import SmallSheep

sheep = SmallSheep()

from SpikeSheepAnimation import SpikeSheepAnimation
from FireSheepAnimation import FireSheepAnimation
from AlternateSheepAnimation import AlternateSheepAnimation
from SheepConfettiAnimation import SheepConfettiAnimation
from RainbowAnimation import RainbowAnimation
from FillFadeSheepAnimation import FillFadeSheepAnimation
from StarsSheepAnimation import StarsSheepAnimation

# animation = SpikeSheepAnimation(sheep, {'hue_start' :0.1})
# animation = FillFadeSheepAnimation(sheep, {'hue_start' : 'Rainbow'})
animation = StarsSheepAnimation(sheep, {'stars_percent' : 0.01})

speed = 75 # in 50 hrz
current_time = 0
frame_id = 0;
    
while True:
        
	time_precent = float(current_time) / speed

	animation.apply(time_precent)

	network.send(sheep_data=sheep.get_array())

	time.sleep(0.02)
	current_time = (current_time + 1) % speed
 	frame_id += 500


