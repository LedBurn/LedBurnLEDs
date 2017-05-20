
import random
import math

from Colors import Colors

class GlowGrassAnimation:

    def __init__(self, grass):
        self.grass = grass

    def apply(self, time_percent):

        if time_percent < 0.5:
            c = time_percent * 0.25
        else:
            c = (1.0 - time_percent) * 0.25
        c = c +0.01
        c = math.pow(c, 0.5)

        for i in self.grass.get_all_indexes():
            self.grass.get_array()[i * 3:i * 3 + 3] = Colors.change_rgb_lightness([32, 64, 0], c)




