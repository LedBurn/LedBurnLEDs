from AbstractEffect import Effect
from GradientEffect import GradientEffect

import math
import random

max_red = 255
min_red = 120

max_green = 130
min_green = 5

red_color_top = [5, 0, 0]
red_color_bottom = [200, 0, 0]


class FireEffect(Effect):

    def __init__(self, indexes):
        Effect.__init__(self, indexes)
        self.num_of_loops = random.randrange(4, 60)
        self.loop_num = 0
        self.create_effects()

    def create_effects(self):
        self.effects = []

        up = self.indexes

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

    
    def apply(self, time_percent, parent_array):
        
        loop = math.floor(time_percent * self.num_of_loops)
        if (loop != self.loop_num):
            self.loop_num =  self.loop_num + 1 if (self.loop_num + 1 < self.num_of_loops) else 0
            self.create_effects()
        
        for effect in self.effects:
            effect.apply(time_percent, parent_array)







