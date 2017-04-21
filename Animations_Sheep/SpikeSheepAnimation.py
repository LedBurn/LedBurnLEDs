from AbstractSheepAnimation import SheepAnimation
from Effects.SpikeEffect import SpikeEffect

from Colors.TimedColor import HueChangeTimedColor

import random

class SpikeSheepAnimation(SheepAnimation):
    def __init__(self, sheep):
        SheepAnimation.__init__(self, sheep)
        self.restart_effect()
        self.previous_time = 1

    def apply(self, time_percent):

        if time_percent < self.previous_time:
            self.restart_effect()
        self.previous_time = time_percent

        for e in self.effects:
            e.apply(time_percent, self.sheep.get_array())

    def restart_effect(self):
        self.effects = []
        all_i = self.sheep.get_body_indexes()
        for i in range(0, self.sheep.get_num_of_body_parts()):
            self.add_spike_effect(self.sheep.get_body_part_indexes(i))

    def add_spike_effect(self, indexes):
        first_i = random.randint(0, len(indexes)/2 - 1)
        first_i = 0
        if random.random() < 0.5:
            indexes = indexes[::-1]
        hue_start = 0
        self.effects.append(SpikeEffect(indexes, HueChangeTimedColor(hue_start, hue_start + 1.0), 1.0, len(indexes) * 2))

