#!/usr/bin/env python

import sys, os

sys.path.append(os.path.abspath('../'))
import Network.LedBurnProtocol as network
import time

from UIElements.Flower import Flower
from UIElements.SmallSheep import SmallSheep

flower = Flower()
sheep = SmallSheep()

from Animations_Flower.ExplosionFlowerAnimation import ExplosionFlowerAnimation
from Animations_Flower.RainbowFlowerAnimation import RainbowFlowerAnimation
from Animations_Flower.AlternateFlowerAnimation import AlternateFlowerAnimation
from Animations_Flower.RoundRobinFlowerAnimation import RoundRobinFlowerAnimation
from Animations_Flower.NaturalFlowerAnimation import NaturalFlowerAnimation
from Animations_Flower.FireFlowerAnimation import FireFlowerAnimation
from Animations_Flower.ConfettiFlowerAnimation import ConfettiFlowerAnimation
from Animations_Flower.GlowFlowerAnimation import GlowFlowerAnimation
from Animations_Flower.SpikesFlowerAnimation import SpikesFlowerAnimation

animations_flower_arr = []
animations_flower_arr.append({'animation': SpikesFlowerAnimation(flower, None), 'speed': 60})
animations_flower_arr.append({'animation': RainbowFlowerAnimation(flower, None), 'speed': 100})
animations_flower_arr.append({'animation': GlowFlowerAnimation(flower, None), 'speed': 60})
animations_flower_arr.append({'animation': FireFlowerAnimation(flower, None), 'speed': 100})
#animations_flower_arr.append({'animation': NaturalFlowerAnimation(flower, None), 'speed': 17})
animations_flower_arr.append({'animation': AlternateFlowerAnimation(flower, None), 'speed': 50})
animations_flower_arr.append({'animation': ConfettiFlowerAnimation(flower, None), 'speed': 15})
animations_flower_arr.append({'animation': ExplosionFlowerAnimation(flower, None), 'speed': 30})
animations_flower_arr.append({'animation': RoundRobinFlowerAnimation(flower, None), 'speed': 30})

from Animations_Sheep.SpikeSheepAnimation import SpikeSheepAnimation
from Animations_Sheep.FireSheepAnimation import FireSheepAnimation
from Animations_Sheep.AlternateSheepAnimation import AlternateSheepAnimation
from Animations_Sheep.SheepConfettiAnimation import SheepConfettiAnimation
from Animations_Sheep.RainbowAnimation import RainbowAnimation
from Animations_Sheep.FillFadeSheepAnimation import FillFadeSheepAnimation
from Animations_Sheep.StarsSheepAnimation import StarsSheepAnimation
from Animations_Sheep.GlowSheepAnimation import GlowSheepAnimation
from Animations_Sheep.FadeInOutAnimation import FadeInOutAnimation

animations_sheep_arr = []
animations_sheep_arr.append({'animation': SpikeSheepAnimation(sheep, None), 'speed': 60})
animations_sheep_arr.append({'animation': RainbowAnimation(sheep, None), 'speed': 100})
animations_sheep_arr.append({'animation': GlowSheepAnimation(sheep), 'speed': 60})
animations_sheep_arr.append({'animation': FireSheepAnimation(sheep, None), 'speed': 60})

animations_sheep_arr.append({'animation': AlternateSheepAnimation(sheep, None), 'speed': 50})
animations_sheep_arr.append({'animation': SheepConfettiAnimation(sheep, None), 'speed': 60})
animations_sheep_arr.append({'animation': FillFadeSheepAnimation(sheep, None), 'speed': 30})
animations_sheep_arr.append({'animation': StarsSheepAnimation(sheep, None), 'speed': 60})

speed_flower = 100  # in 50 hrz
animation_flower = None
current_time_flower = 0
animation_time_flower = 0

animation_sheep = None

animation_index = 0
def set_new_animation():
    global animation_index, \
        animation_flower, speed_flower, current_time_flower, animation_time_flower, \
        animation_sheep, speed_sheep, current_time_sheep, animation_time_sheep

    animation_index = animation_index + 1

    animation_obj = animations_flower_arr[animation_index % len(animations_flower_arr)]
    animation_flower = animation_obj['animation']
    speed_flower = animation_obj['speed']
    current_time_flower = 0
    animation_time_flower = 0

    animation_obj = animations_sheep_arr[animation_index % len(animations_sheep_arr)]
    animation_sheep = animation_obj['animation']
    speed_sheep = animation_obj['speed']
    current_time_sheep = 0
    animation_time_sheep = 0


set_new_animation()
while True:

    if animation_time_flower > 600:
        set_new_animation()

    time_precent_flower = float(current_time_flower) / speed_flower
    animation_flower.apply(time_precent_flower)

    time_precent_sheep = float(current_time_sheep) / speed_sheep
    animation_sheep.apply(time_precent_sheep)

    network.send(flower_data=flower.get_array(), sheep_data=sheep.get_array())

    time.sleep(0.03)
    current_time_flower = (current_time_flower + 1) % speed_flower
    animation_time_flower = animation_time_flower + 1
    current_time_sheep = (current_time_sheep + 1) % speed_sheep
    animation_time_sheep = animation_time_sheep + 1


