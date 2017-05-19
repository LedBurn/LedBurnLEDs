from AbstractTreeAnimation import TreeAnimation

from Effects.RainbowEffect import RainbowEffect

from Colors import Colors

import random

class RainbowTreeAnimation(TreeAnimation):

    def __init__(self, tree, props):
        TreeAnimation.__init__(self, tree, props)
        self.effects = []
        for leaf in self.tree.get_leaves_and_stem():
            self.effects.append(RainbowEffect(leaf[0][::-1]))
            self.effects.append(RainbowEffect(leaf[1][::-1]))

    def apply(self, time_percent):
        for effect in self.effects:
            effect.apply(time_percent, self.tree.get_array())




