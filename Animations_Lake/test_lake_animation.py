#!/usr/bin/env python

import sys, os
sys.path.append(os.path.abspath('../'))
import time

import Network.LedBurnProtocol as network

from UIElements.Lake import Lake

lake = Lake()

from RoundRobinLakeAnimation import RoundRobinLakeAnimation
from ConfettiLakeAnimation import ConfettiLakeAnimation
from NaturalLakeAnimation import NaturalLakeAnimation
from EqLakeAnimation import EqLakeAnimation
from SpiningColorLakeAnimation import SpiningColorLakeAnimation
from StarsLakeAnimation import StarsLakeAnimation
animation = SpiningColorLakeAnimation(lake,None)

speed = 100 # in 50 hrz
current_time = 0
frame_id = 0
    
while True:
        
	time_precent = float(current_time) / speed

	animation.apply(time_precent)

	network.send(frame_id, lake_data=lake.get_array())

	time.sleep(0.05)
	current_time = (current_time + 1) % speed
 	frame_id += 500


