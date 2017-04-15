from AbstractSheepAnimation import SheepAnimation

import sys, os
sys.path.append(os.path.abspath('../UIElements'))
from AbstractSheep import Sheep

sys.path.append(os.path.abspath('../Effects'))
from FireEffect import FireEffect
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

        self.effects = []
        
        self.effects.append(AlwaysOnEffect(self.sheep.get_ears_indexes(), [255, 0 ,0]))

        self.effects.append(FireEffect(self.sheep.get_leg12_side1_indexes()[::-1]))
        self.effects.append(FireEffect(self.sheep.get_leg12_side2_indexes()))
        self.effects.append(FireEffect(self.sheep.get_leg34_side1_indexes()[::-1]))
        self.effects.append(FireEffect(self.sheep.get_leg34_side2_indexes()))

        self.effects.append(FireEffect(self.sheep.get_head_up1()))
        self.effects.append(FireEffect(self.sheep.get_head_up2()))

        for i in range(self.sheep.get_num_of_body_parts()):
            body_part = self.sheep.get_body_part_indexes(i)

            if i < 4 :
                up = body_part[:len(body_part)/2]
                down = body_part[len(body_part)/2:]

                self.effects.append(FireEffect(up[::-1]))
                self.effects.append(FireEffect(down))

            elif i == 4:
                continue

            elif i == 5:
                body_part4 = self.sheep.get_body_part_indexes(4)
                
                up = body_part[:len(body_part)/2]
                up = body_part4 + up
                down = body_part[len(body_part)/2:]

                self.effects.append(FireEffect(up))
                self.effects.append(FireEffect(down[::-1]))

            elif i > 5 :
                up = body_part[:len(body_part)/2]
                down = body_part[len(body_part)/2:]

                self.effects.append(FireEffect(up))
                self.effects.append(FireEffect(down[::-1]))


    def apply(self, time_percent):
        
        for effect in self.effects:
            effect.apply(time_percent, self.sheep.get_array())







