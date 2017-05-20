
import random
import math
from Effects.SpikeEffect import SpikeEffect
from Colors.TimedColor import ConstTimedColor

from Colors import Colors

class GlowSheepAnimation:

    def __init__(self, sheep):
        self.sheep = sheep
        self.head_spike = None
        self.is_input_mode = False

    def apply(self, time_percent):

        if time_percent < 0.5:
            c = time_percent * 0.25
        else:
            c = (1.0 - time_percent) * 0.25
        c = c +0.01
        c = math.pow(c, 0.5)

        for i in self.sheep.get_all_indexes():
            self.sheep.get_array()[i*3:i*3+3] = Colors.change_rgb_lightness([64, 64, 64], c)

        if self.head_spike is not None:
            time_percent = (time_percent % 0.25) * 4.0
            self.head_spike.apply(time_percent, self.sheep.get_array())

    def set_is_input_mode(self, val):
        if self.is_input_mode == val:
            return
        if val:
            self.head_spike = SpikeEffect(self.sheep.get_head_indexes(), ConstTimedColor([255, 0, 0]), 1.0, len(self.sheep.get_head_indexes()), True)
        else:
            self.head_spike = None
        self.is_input_mode = val

