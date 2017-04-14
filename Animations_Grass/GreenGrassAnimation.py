from GrassAnimation import GrassAnimation

import sys, os
sys.path.append(os.path.abspath('../UIElements'))
from Grass import Grass

sys.path.append(os.path.abspath('../Effects'))
from GradientEffect import GradientEffect

import math
import random

num_of_loops = 16
max_green = 200
min_green = 5

class GreenGrassAnimation(GrassAnimation):

    def __init__(self, grass):
        GrassAnimation.__init__(self, grass)
        self.create_effects()
        self.loop_num = 0

    def create_effects(self):
        self.effects = []

        for leaf in self.grass.get_leaves_array():
            up = leaf[0]
            down = leaf[1]

            max = max_green - random.randrange(50)
            min = min_green + random.randrange(10)

            max_color = [0, max, 0]
            min_color = [0, min, 0]

            self.effects.append(GradientEffect(up[::-1], min_color, max_color, 4))
            self.effects.append(GradientEffect(down, min_color, max_color, 4))
    

    def apply(self, time_percent):
        
        loop = math.floor(time_percent * num_of_loops)
        if (loop != self.loop_num):
            self.loop_num =  self.loop_num + 1 if (self.loop_num + 1 < num_of_loops) else 0
            self.create_effects()
        
        for effect in self.effects:
            effect.apply(time_percent, self.grass.get_array())







