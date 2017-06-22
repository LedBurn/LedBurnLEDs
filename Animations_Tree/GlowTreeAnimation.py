
import random
import math

from Colors import Colors

class GlowTreeAnimation:

    def __init__(self, tree):
        self.tree = tree

    def apply(self, time_percent):

        if time_percent < 0.5:
            c = time_percent * 0.25
        else:
            c = (1.0 - time_percent) * 0.25
        c = c +0.01
        c = math.pow(c, 0.5)

        for i in self.tree.get_stem():
            self.tree.get_array()[i*3:i*3+3] = Colors.change_rgb_lightness([184, 134, 11], c)
        for i in self.tree.get_leaves():
            self.tree.get_array()[i*3:i*3+3] = Colors.change_rgb_lightness([0, 255, 0], c)

