from AbstractTreeAnimation import TreeAnimation

from Effects.GoToColorEffect import GoToColorEffect, GoToColorEffectType
from Effects.AdvanceEffect import AdvanceEffect
from Effects.AlwaysOnEffect import AlwaysOnEffect

from Colors import Colors

import random

class ExplosionTreeAnimation(TreeAnimation):

    def __init__(self, tree, props):
        TreeAnimation.__init__(self, tree, props)
        self.previous_time = 1;
        self.frame_counter = 0
        self.color = [0, 0, 0]
        self.previous_color = [0, 0, 0]
        self.previous_hue = 0
        self.effects = []

    def apply(self, time_percent):

        if (time_percent < self.previous_time):
            self.effects = []

            if self.frame_counter % 2 == 0:
                hue = self.previous_hue + 0.1 + random.random() * 0.8
                if hue > 1: hue -= 1
                self.previous_hue = hue
                self.previous_color = self.color
                self.color = Colors.hls_to_rgb(hue, 1, 1)

                self.effects.append(AdvanceEffect.initColor(self.tree.get_right_stem(), self.previous_color, self.color))
                self.effects.append(AdvanceEffect.initColor(self.tree.get_left_stem(), self.previous_color, self.color))

                for leaf in self.tree.get_leaves_array():
                    self.effects.append(
                        AlwaysOnEffect(leaf[0], self.previous_color))
                    self.effects.append(
                        AlwaysOnEffect(leaf[1], self.previous_color))

            if self.frame_counter % 2 == 1:
                self.effects.append(AlwaysOnEffect(self.tree.get_right_stem(), self.color))
                self.effects.append(AlwaysOnEffect(self.tree.get_left_stem(), self.color))

                for leaf in self.tree.get_leaves_array():
                    self.effects.append(
                        AdvanceEffect.initColor(leaf[0][::-1], self.previous_color, self.color))
                    self.effects.append(
                        AdvanceEffect.initColor(leaf[1][::-1], self.previous_color, self.color))

            self.frame_counter += 1

        for effect in self.effects:
            effect.apply(time_percent, self.tree.get_array())

        self.previous_time = time_percent



