import random
from GrassAnimation import GrassAnimation
from Colors.TimedColor import ConstTimedColor, TimedColorFactory
from Effects.StarEffect import StarEffect

class StarsGrassAnimation(GrassAnimation):

    def __init__(self, grass, props):
        GrassAnimation.__init__(self, grass, props)

        self.effects = []
        self.previous_time = 0

        stars_percent = props['stars_percent'] if props and 'stars_percent' in props else 0.1
        self.stars_per_cycle = int(stars_percent * len(self.grass.get_leaves()))
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
            effect.apply(time_percent, self.grass.get_array())

    def restart_effect(self):
        self.effects = []
        self.grass.clear()
        indexes = self.grass.get_leaves()[:]
        random.shuffle(indexes)
        for i in range(0, self.stars_per_cycle):
            location_percent = float(i) / float(self.stars_per_cycle)
            self.add_effect_for_index(indexes.pop(), location_percent)


    def add_effect_for_index(self, index, location_percent):
        start_t = random.uniform(0.0, 0.4)
        dark_time = 1.0 - random.uniform(0.00, 0.4)
        on_tot_time = dark_time - start_t
        on_start_t = start_t + random.uniform(0.1, on_tot_time / 2.0)
        on_end_t = dark_time - random.uniform(0.1, on_tot_time / 2.0)
        self.effects.append(
            StarEffect([index], self.timed_color, start_t, on_start_t, on_end_t, dark_time, location_percent))



