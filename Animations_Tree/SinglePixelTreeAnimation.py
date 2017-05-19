
from AbstractTreeAnimation import TreeAnimation

from Effects.SinglePixelEffect import SinglePixelEffect

from Colors import Colors

import random

class SinglePixelTreeAnimation(TreeAnimation):

    def __init__(self, tree, props):
        TreeAnimation.__init__(self, tree, props)
        self.effects = []
        self.last_time = 0
        self.create_effects()

    def create_effects(self):
        self.effects = []
        hue = random.random()
        for leaf in self.tree.get_leaves_and_stem():
            self.effects.append(SinglePixelEffect(leaf[0][::-1], [0,0,0], Colors.hls_to_rgb(hue, 1.0, 1.0), len(leaf[0])))
            self.effects.append(SinglePixelEffect(leaf[1][::-1], [0,0,0], Colors.hls_to_rgb(hue, 1.0, 1.0), len(leaf[1])))

    def apply(self, time_percent):
        if time_percent < self.last_time:
            self.create_effects()
        self.last_time = time_percent
        corr_percent = time_percent * 2 if time_percent <= 0.5 else 2.0- time_percent * 2
        for effect in self.effects:
            effect.apply(corr_percent, self.tree.get_array())




