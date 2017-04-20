from FlowerAnimation import FlowerAnimation

from Effects.AlwaysOnEffect import AlwaysOnEffect

from Colors import Colors

import random

class RoundRobinFlowerAnimation(FlowerAnimation):

    def __init__(self, flower, props):
        FlowerAnimation.__init__(self, flower, props)
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
            effect.apply(time_percent, self.flower.get_array())

    def _start_spike(self):

        self.effects = []
        self.last_hue += self.hue_speed
        if self.last_hue > 1:
            self.last_hue -= 1
        rand_color = Colors.hls_to_rgb(self.last_hue, 1.0, 1.0)
        self.effects.append(AlwaysOnEffect(self.flower.get_leaves_array()[self.last_leaf], rand_color))
        self.effects.append(AlwaysOnEffect(self.flower.seeds, rand_color))
        self.effects.append(AlwaysOnEffect(self.flower.bottom_parts, rand_color))

        self.last_leaf += 1
        if self.last_leaf >= len(self.flower.get_leaves_array()):
            self.last_leaf = 0




