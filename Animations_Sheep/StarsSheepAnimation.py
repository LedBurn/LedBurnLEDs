from AbstractSheepAnimation import SheepAnimation
from Effects.StarEffect import StarEffect

from Colors.TimedColor import ConstTimedColor
from Colors import Colors

import random

class StarsSheepAnimation(SheepAnimation):
    def __init__(self, sheep, props):
        SheepAnimation.__init__(self, sheep)

        stars_percent = props['stars_percent'] if props and 'stars_percent' in props else 0.1
        self.stars_per_cycle = int(stars_percent * len(sheep.get_array()))

        self.previous_time = 1.0

        self.restart_effect()

    def apply(self, time_percent):

        if time_percent < self.previous_time:
            self.restart_effect()
        self.previous_time = time_percent

        for e in self.effects:
            e.apply(time_percent, self.sheep.get_array())

    def restart_effect(self):
        self.effects = []
        self.sheep.clear()
        indexes = self.sheep.get_all_indexes()[:]
        random.shuffle(indexes)
        #always include the sheep eyes
        for i in self.sheep.get_ears_indexes():
            self.add_effect_for_index(i)
        for _ in range(0, self.stars_per_cycle):
            self.add_effect_for_index(indexes.pop())

    def add_effect_for_index(self, index):
        start_t = random.uniform(0.0, 0.4)
        dark_time = 1.0 - random.uniform(0.00, 0.4)
        on_tot_time = dark_time - start_t
        on_start_t = start_t + random.uniform(0.1, on_tot_time / 2.0)
        on_end_t = dark_time - random.uniform(0.1, on_tot_time / 2.0)
        rgb_color = Colors.hls_to_rgb(random.random(), random.uniform(0, 0.5), 1.0)
        self.effects.append(
            StarEffect([index], ConstTimedColor(rgb_color), start_t, on_start_t, on_end_t, dark_time))

