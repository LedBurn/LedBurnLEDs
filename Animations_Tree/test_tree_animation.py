#!/usr/bin/env python

import sys, os

sys.path.append(os.path.abspath('../'))
import Network.LedBurnProtocol as network
import time

from UIElements.Tree import Tree

tree = Tree()

from ConfettiTreeAnimation import ConfettiTreeAnimation
from AlternateTreeAnimation import AlternateTreeAnimation
from RoundRobinTreeAnimation import RoundRobinTreeAnimation
from ExplotionTreeAnimation import  ExplosionTreeAnimation
from RainbowTreeAnimation import RainbowTreeAnimation
from FireTreeAnimation import FireTreeAnimation
from NaturalTreeAnimation import NaturalTreeAnimation
from SpikeTreeAnimation import SpikeTreeAnimation
from SinglePixelTreeAnimation import SinglePixelTreeAnimation

#animation = RoundRobinTreeAnimation(tree, {})
#animation = AlternateTreeAnimation(tree, {})
#animation = ConfettiTreeAnimation(tree, {})
#animation = ExplosionTreeAnimation(tree, {})
#animation = RainbowTreeAnimation(tree, {})
#animation = FireTreeAnimation(tree, {})
#animation = NaturalTreeAnimation(tree, {})
#animation = SpikeTreeAnimation(tree, {'circular': False, 'dir': 'outside'})
animation = SinglePixelTreeAnimation(tree, {})

speed = 25  # in 50 hrz
current_time = 0
frame_id = 0;

while True:
    time_precent = float(current_time) / speed

    animation.apply(time_precent)

    network.send(frame_id, tree_data=tree.get_array())

    time.sleep(0.02)
    current_time = (current_time + 1) % speed
    frame_id += 500


