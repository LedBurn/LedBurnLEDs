import random
from Colors import Colors
from AbstractTreeAnimation import TreeAnimation
from Effects.AlternateColorEvery3Effect import AlternateColorEvery3Effect
from Effects.AlwaysOnEffect import AlwaysOnEffect


class AlternateTreeAnimation(TreeAnimation):
    def __init__(self, tree, props):
        TreeAnimation.__init__(self, tree, props)
        self.previous_time = 1
        self.effects = []
        self.cycle_num = 0

    def random_hue(self):
        self.hue1 = random.random()
        self.hue2 = self.hue1 + 0.3 + random.random() * 0.4
        if self.hue2 > 1: self.hue2 - 1

    def create_effects(self):
        self.effects = []

        color1 = Colors.hls_to_rgb(self.hue1, 1, 1)
        color2 = Colors.hls_to_rgb(self.hue2, 1, 1)
        self.effects.append(AlternateColorEvery3Effect(self.tree.get_all_indexes(), color1, color2))

    def apply(self, time_percent):
        if (time_percent < self.previous_time):

            if (self.cycle_num % 4 == 0):
                self.random_hue()
                self.create_effects()

            self.cycle_num += 1

        for effect in self.effects:
            effect.apply(time_percent, self.tree.get_array())

        self.previous_time = time_percent
