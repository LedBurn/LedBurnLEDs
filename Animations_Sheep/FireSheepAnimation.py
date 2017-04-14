from AbstractSheepAnimation import SheepAnimation

import sys, os
sys.path.append(os.path.abspath('../UIElements'))
from AbstractSheep import Sheep

sys.path.append(os.path.abspath('../Effects'))
from GradientEffect import GradientEffect
from AlwaysOnEffect import AlwaysOnEffect

import math
import random

max_red = 255
min_red = 120

max_green = 130
min_green = 5

red_color_top = [5, 0, 0]
red_color_bottom = [200, 0, 0]

class FireSheepAnimation(SheepAnimation):

    def __init__(self, sheep):
        SheepAnimation.__init__(self, sheep)
        self.num_of_loops = random.randrange(4, 60)
        self.create_effects()
        self.loop_num = 0
        self.eyes_effect = AlwaysOnEffect(self.sheep.get_ears_indexes(), [255, 0 ,0])

    def create_effects(self):
        self.effects = []

        self.fire_elements = []
        self.fire_elements.append(self.sheep.get_leg12_side1_indexes()[::-1])
        self.fire_elements.append(self.sheep.get_leg12_side2_indexes())
        self.fire_elements.append(self.sheep.get_leg34_side1_indexes()[::-1])
        self.fire_elements.append(self.sheep.get_leg34_side2_indexes())

        self.fire_elements.append(self.sheep.get_head_up1())
        self.fire_elements.append(self.sheep.get_head_up2())

        for i in range(self.sheep.get_num_of_body_parts()):
            body_part = self.sheep.get_body_part_indexes(i)

            if i < 4 :
                up = body_part[:len(body_part)/2]
                down = body_part[len(body_part)/2:]

                self.fire_elements.append(up[::-1])
                self.fire_elements.append(down)

            elif i == 4:
                continue

            elif i == 5:
                body_part4 = self.sheep.get_body_part_indexes(4)
                
                up = body_part[:len(body_part)/2]
                up = body_part4 + up
                down = body_part[len(body_part)/2:]

                self.fire_elements.append(up)
                self.fire_elements.append(down[::-1])

            elif i > 5 :
                up = body_part[:len(body_part)/2]
                down = body_part[len(body_part)/2:]

                self.fire_elements.append(up)
                self.fire_elements.append(down[::-1])

        self.fire_elements.append(self.sheep.get_leg34_side2_indexes())

        for up in self.fire_elements:

            max_r = max_red - random.randrange(100)
            min_r = min_red + random.randrange(100)

            max_g = max_green - random.randrange(50)
            min_g = min_green + random.randrange(10)

            if (min_g > min_r + 20):
                min_r = min_g + 20

            max_color = [max_r, max_g, 0]
            min_color = [min_r, min_g, 0]

            fire_level = len(up) - random.randrange(int(len(up)*0.8))
            if (fire_level < 5):
                fire_level = 5

            up_flame_top = up[fire_level::]
            self.effects.append(GradientEffect(up_flame_top[::-1], red_color_top, min_color, 4))

            up_flame = up[2:fire_level:]
            self.effects.append(GradientEffect(up_flame[::-1], min_color, max_color, 4))

            up_fire = up[:2:]
            self.effects.append(GradientEffect(up_fire, red_color_bottom, max_color, 4))

    def apply(self, time_percent):
        
        loop = math.floor(time_percent * self.num_of_loops)
        if (loop != self.loop_num):
            self.loop_num =  self.loop_num + 1 if (self.loop_num + 1 < self.num_of_loops) else 0
            self.create_effects()
        
        for effect in self.effects:
            effect.apply(time_percent, self.sheep.get_array())

        self.eyes_effect.apply(time_percent, self.sheep.get_array())







