from GrassAnimation import GrassAnimation

import random, colorsys

from Effects.AlwaysOnEffect import AlwaysOnEffect

from Colors import Colors


class RoundRobinGrassAnimation(GrassAnimation):
    def __init__(self, grass, props):
        GrassAnimation.__init__(self, grass, props)
        self.effects = []
        self.last_leaf = 0
        self.previous_time = 1

        self.hue_speed = 0.05
        self.last_hue = random.random()
        if self.props != None:
            if 'hue_speed' in self.props:
                self.hue_speed = self.props['hue_speed']
            if 'hue_start' in self.props:
                self.last_hue = self.props['hue_start']

    def apply(self, time_percent):

        if time_percent < self.previous_time:
            self._start_spike()
        self.previous_time = time_percent


        for effect in self.effects:
            effect.apply(time_percent, self.grass.get_array())

    def _start_spike(self):

        self.effects = []
        self.last_hue += self.hue_speed
        if self.last_hue > 1:
            self.last_hue -= 1
        rand_color = Colors.hls_to_rgb(self.last_hue, 1.0, 1.0)
        new_animation = AlwaysOnEffect(self.grass.get_leaves_array()[self.last_leaf][0] + self.grass.get_leaves_array()[self.last_leaf][1], rand_color)
        self.effects.append(new_animation)

        self.last_leaf += 1
        if self.last_leaf >= len(self.grass.get_leaves_array()):
            self.last_leaf = 0

