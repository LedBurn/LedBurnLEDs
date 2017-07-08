#!/usr/bin/env python

import sys, os

sys.path.append(os.path.abspath('../'))
import Network.LedBurnProtocol as network
import time

from UIElements.Flower import Flower

flower = Flower()

from Animations_Flower.ExplosionFlowerAnimation import ExplosionFlowerAnimation
from Animations_Flower.RainbowFlowerAnimation import RainbowFlowerAnimation
from Animations_Flower.AlternateFlowerAnimation import AlternateFlowerAnimation
from Animations_Flower.RoundRobinFlowerAnimation import RoundRobinFlowerAnimation
from Animations_Flower.NaturalFlowerAnimation import NaturalFlowerAnimation
from Animations_Flower.FireFlowerAnimation import FireFlowerAnimation
from Animations_Flower.ConfettiFlowerAnimation import ConfettiFlowerAnimation
from Animations_Flower.GlowFlowerAnimation import GlowFlowerAnimation
from Animations_Flower.SpikesFlowerAnimation import SpikesFlowerAnimation

animations_arr = []
animations_arr.append({'animation': SpikesFlowerAnimation(flower, None), 'speed': 60})
animations_arr.append({'animation': RainbowFlowerAnimation(flower, None), 'speed': 100})
animations_arr.append({'animation': GlowFlowerAnimation(flower, None), 'speed': 60})
animations_arr.append({'animation': FireFlowerAnimation(flower, None), 'speed': 100})
animations_arr.append({'animation': NaturalFlowerAnimation(flower, None), 'speed': 17})
animations_arr.append({'animation': AlternateFlowerAnimation(flower, None), 'speed': 50})
animations_arr.append({'animation': ConfettiFlowerAnimation(flower, None), 'speed': 15})
animations_arr.append({'animation': ExplosionFlowerAnimation(flower, None), 'speed': 30})
animations_arr.append({'animation': RoundRobinFlowerAnimation(flower, None), 'speed': 30})

# animation = ConfettiFlowerAnimation(flower, None)
# animation = SpikesFlowerAnimation(flower, {'color':{'type':'const_color', 'hue':0.5}})
# animation = SpikesFlowerAnimation(flower, None)
# animation = ExplosionFlowerAnimation(flower, None)

speed = 100  # in 50 hrz
animation = None
current_time = 0
animation_time = 0

animation_index = 0
def set_new_animation():
    global animation_index, animation, speed, current_time, animation_time
    animation_index = (animation_index + 1) % len(animations_arr)
    animation_obj = animations_arr[animation_index]
    animation = animation_obj['animation']
    speed = animation_obj['speed']
    current_time = 0
    animation_time = 0


set_new_animation()
while True:

    if animation_time > 600:
        set_new_animation()

    time_precent = float(current_time) / speed
    animation.apply(time_precent)

    network.send(flower_data=flower.get_array())

    time.sleep(0.03)
    current_time = (current_time + 1) % speed
    animation_time = animation_time + 1


