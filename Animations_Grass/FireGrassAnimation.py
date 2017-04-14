from GrassAnimation import GrassAnimation

import sys, os
sys.path.append(os.path.abspath('../UIElements'))
from Grass import Grass

sys.path.append(os.path.abspath('../Effects'))
from GradientEffect import GradientEffect

import math
import random

max_red = 255
min_red = 120

max_green = 130
min_green = 5

red_color_top = [5, 0, 0]
red_color_bottom = [200, 0, 0]

class FireGrassAnimation(GrassAnimation):

    def __init__(self, grass):
        GrassAnimation.__init__(self, grass)
        self.num_of_loops = random.randrange(4, 60)
        self.create_effects()
        self.loop_num = 0

    def create_effects(self):
        self.effects = []

        for leaf in self.grass.get_leaves_array():
            up = leaf[0]
            down = leaf[1][::-1]

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
            down_flame_top = down[fire_level:]
            self.effects.append(GradientEffect(up_flame_top[::-1], red_color_top, min_color, 4))
            self.effects.append(GradientEffect(down_flame_top[::-1], red_color_top, min_color, 4))

            up_flame = up[4:fire_level:]
            down_flame = down[4:fire_level:]
            self.effects.append(GradientEffect(up_flame[::-1], min_color, max_color, 4))
            self.effects.append(GradientEffect(down_flame[::-1], min_color, max_color, 4))


            up_fire = up[:4:]
            down_fire = up[:4:]
            self.effects.append(GradientEffect(up_fire, red_color_bottom, max_color, 4))
            self.effects.append(GradientEffect(down_fire, red_color_bottom, max_color, 4))
    

    def apply(self, time_percent):
        
        loop = math.floor(time_percent * self.num_of_loops)
        if (loop != self.loop_num):
            self.loop_num =  self.loop_num + 1 if (self.loop_num + 1 < self.num_of_loops) else 0
            self.create_effects()
        
        for effect in self.effects:
            effect.apply(time_percent, self.grass.get_array())







