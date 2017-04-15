from GrassAnimation import GrassAnimation

import sys, os
sys.path.append(os.path.abspath('../Effects'))
from SinglePixelEffect import SinglePixelEffect


sys.path.append(os.path.abspath('../Colors'))
from Colors import Colors

import random, colorsys

class HorLineGrassAnimation(GrassAnimation):

    def __init__(self, grass, on_time_percent):
        GrassAnimation.__init__(self, grass)
        self.effects = []

        max_height = 0
        for leaf in self.grass.get_leaves_array():
            max_height = max(max_height, len(leaf[0]))
            max_height = max(max_height, len(leaf[1]))

        for leaf in self.grass.get_leaves_array():
            rand_leaf_color = [int(c*255) for c in colorsys.hsv_to_rgb(0.33, random.uniform(0.35, 1), random.uniform(0.35, 1))]
            self.effects.append(SinglePixelEffect(leaf[0], rand_leaf_color, [0, 255, 255], max_height * (1 + on_time_percent)))
            self.effects.append(SinglePixelEffect(leaf[1][::-1], rand_leaf_color, [0, 255, 255], max_height * (1 + on_time_percent)))

    def apply(self, time_percent):

        for effect in self.effects:
            effect.apply(time_percent, self.grass.get_array())



