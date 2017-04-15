from FlowerAnimation import FlowerAnimation

import sys, os
sys.path.append(os.path.abspath('../UIElements'))
from Flower import Flower

sys.path.append(os.path.abspath('../Effects'))
from GoToColorEffect import GoToColorEffect
from AlwaysOnEffect import AlwaysOnEffect

sys.path.append(os.path.abspath('../'))
from Colors import Colors

import random

class NaturalFlowerAnimation(FlowerAnimation):

    def __init__(self, flower):
        FlowerAnimation.__init__(self, flower)
        self.effects = []
        self.hue = random.random()
        self.previous_time = 1

    def apply(self, time_percent):

        if time_percent < self.previous_time:
            self.next_hue()
        self.previous_time = time_percent

        for effect in self.effects:
            effect.apply(time_percent, self.flower.get_array())

    def next_hue(self):
        self.effects = []

        new_hue = self.hue + 0.03125
        if new_hue > 1 : new_hue -= 1
        prev_color = Colors().hls_to_rgb(self.hue, 1.0, 1.0)
        new_color = Colors().hls_to_rgb(new_hue, 1.0, 1.0)
        self.effects.append(GoToColorEffect(self.flower.get_leaves() + self.flower.seeds, prev_color, new_color))
        self.hue = new_hue

        self.effects.append(AlwaysOnEffect(self.flower.line, [50, 200, 0]))
        self.effects.append(AlwaysOnEffect(self.flower.leaves, [0, 200, 0]))






