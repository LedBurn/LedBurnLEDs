from GrassAnimation import GrassAnimation

import sys, os, random, colorsys

sys.path.append(os.path.abspath('../UIElements'))
from Grass import Grass

sys.path.append(os.path.abspath('../Effects'))
from AlwaysOnEffect import AlwaysOnEffect


class RoundRobinGrassAnimation(GrassAnimation):
    def __init__(self, grass):
        GrassAnimation.__init__(self, grass)
        self.effects = []
        self.last_hue = 0.0
        self.last_leaf = 0
        self.previous_time = 1

    def apply(self, time_percent):

        if time_percent < self.previous_time:
            self._start_spike()
        self.previous_time = time_percent


        for effect in self.effects:
            effect.apply(time_percent, self.grass.get_array())

    def _start_spike(self):

        self.effects = []
        self.last_hue += 0.05
        rand_color = [ int(c * 255) for c in colorsys.hsv_to_rgb(self.last_hue, 1.0, 1.0)]
        new_animation = AlwaysOnEffect(self.grass.get_leaves_array()[self.last_leaf][0] + self.grass.get_leaves_array()[self.last_leaf][1], rand_color)
        self.effects.append(new_animation)

        self.last_leaf += 1
        if self.last_leaf >= len(self.grass.get_leaves_array()):
            self.last_leaf = 0

