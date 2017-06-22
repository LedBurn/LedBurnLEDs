
import random
import math

from Colors import Colors

class GlowFlowerAnimation:

    def __init__(self, flower, props):
        self.flower = flower

    def apply(self, time_percent):

        if time_percent < 0.5:
            c = time_percent * 0.25
        else:
            c = (1.0 - time_percent) * 0.25
        c = c +0.01
        c = math.pow(c, 0.5)

        for i in self.flower.get_leaves():
            self.flower.get_array()[i*3:i*3+3] = Colors.change_rgb_lightness([128, 0, 128], c)
        for i in self.flower.get_seeds():
            self.flower.get_array()[i*3:i*3+3] = Colors.change_rgb_lightness([255, 255, 0], c)
        for i in self.flower.bottom_parts:
            self.flower.get_array()[i*3:i*3+3] = Colors.change_rgb_lightness([0, 255, 0], c)

