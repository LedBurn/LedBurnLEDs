from FlowerAnimation import FlowerAnimation

import sys, os
sys.path.append(os.path.abspath('../UIElements'))
from Flower import Flower

sys.path.append(os.path.abspath('../Effects'))
from AlwaysOnEffect import AlwaysOnEffect

sys.path.append(os.path.abspath('../Colors'))
from Colors import Colors

import random

class RoundRobinFlowerAnimation(FlowerAnimation):

    def __init__(self, flower):
        FlowerAnimation.__init__(self, flower)
        self.effects = []
        self.last_hue = 0.0
        self.last_leaf = 0
        self.previous_time = 1

    def apply(self, time_percent):

        if time_percent < self.previous_time:
            self._start_spike()
        self.previous_time = time_percent

        for effect in self.effects:
            effect.apply(time_percent, self.flower.get_array())

    def _start_spike(self):

        self.effects = []
        self.last_hue += 0.05
        rand_color = Colors().hls_to_rgb(self.last_hue, 1.0, 1.0)
        self.effects.append(AlwaysOnEffect(self.flower.get_leaves_array()[self.last_leaf], rand_color))
        self.effects.append(AlwaysOnEffect(self.flower.seeds, rand_color))
        self.effects.append(AlwaysOnEffect(self.flower.bottom_parts, rand_color))

        self.last_leaf += 1
        if self.last_leaf >= len(self.flower.get_leaves_array()):
            self.last_leaf = 0




