#!/usr/bin/env python

import sys, os
sys.path.append(os.path.abspath('../'))
import Network.LedBurnProtocol as network
import time

from UIElements.Grass import Grass

grass = Grass()

from FireGrassAnimation import FireGrassAnimation
from RoundRobinGrassAnimation import RoundRobinGrassAnimation
from ConfettiGrassAnimation import ConfettiGrassAnimation
from SpikeGrassAnimation import SpikeGrassAnimation
from StarsGrassAnimation import StarsGrassAnimation
from SwipeGrassAnimation import SwipeGrassAnimation

# animation = ConfettiGrassAnimation(grass, None)
#animation = SwipeGrassAnimation(grass, {'color': {'type': 'timed_hue', 'hue_start' : 0.0, 'hue_end' : 1.5}})
animation = SwipeGrassAnimation(grass, {})

speed = 75 # in 50 hrz
current_time = 0
frame_id = 0
    
while True:
        
	time_precent = float(current_time) / speed

	animation.apply(time_precent)

	network.send(frame_id, grass_data=grass.get_array())

	time.sleep(0.02)
	current_time = (current_time + 1) % speed
 	frame_id += 500


