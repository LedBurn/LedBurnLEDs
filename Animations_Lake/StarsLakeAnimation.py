from LakeAnimation import LakeAnimation

from Effects.StarEffect import StarEffect
from Colors.TimedColor import TimedColorFactory, ConstTimedColor
from Colors import Colors

import random

class StarsLakeAnimation(LakeAnimation):
    def __init__(self, lake, props):
        LakeAnimation.__init__(self, lake, props)
        self.effects = []

        self.previous_time = 0

        stars_percent = props['stars_percent'] if props and 'stars_percent' in props else 0.1
        self.stars_per_cycle = int(stars_percent * len(self.lake.whole_lake))
        self.timed_color = ConstTimedColor([255, 255, 255])

        if self.props != None:
            if 'stars_color' in self.props:
                timed_color = TimedColorFactory(self.props['stars_color'])
                if timed_color is not None:
                    self.timed_color = timed_color


        self.restart_effect()

    def apply(self, time_percent):

        if time_percent < self.previous_time:
            self.restart_effect()
        self.previous_time = time_percent

        for effect in self.effects:
            effect.apply(time_percent, self.lake.get_array())

    def restart_effect(self):
        self.effects = []
        self.lake.clear()
        indexes = self.lake.whole_lake[:]
        random.shuffle(indexes)
        for i in range(0, self.stars_per_cycle):
            location_percent = float(i) / len(self.stars_per_cycle)
            self.add_effect_for_index(indexes.pop(), location_percent)


    def add_effect_for_index(self, index, location_percent):
        start_t = random.uniform(0.0, 0.4)
        dark_time = 1.0 - random.uniform(0.00, 0.4)
        on_tot_time = dark_time - start_t
        on_start_t = start_t + random.uniform(0.1, on_tot_time / 2.0)
        on_end_t = dark_time - random.uniform(0.1, on_tot_time / 2.0)
        rgb_color = Colors.hls_to_rgb(random.random(), random.uniform(0, 0.5), 1.0)
        self.effects.append(
            StarEffect([index], self.timed_color, start_t, on_start_t, on_end_t, dark_time, location_percent))
