from LakeAnimation import LakeAnimation

import sys, os, random, colorsys

sys.path.append(os.path.abspath('../UIElements'))
from Lake import Lake

sys.path.append(os.path.abspath('../Effects'))
from AlwaysOnEffect import AlwaysOnEffect

sys.path.append(os.path.abspath('../'))
from Colors import Colors


class RoundRobinLakeAnimation(LakeAnimation):
    def __init__(self, lake, props):
        LakeAnimation.__init__(self, lake, props)
        self.effects = []
        self.last_wave = 0
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
            effect.apply(time_percent, self.lake.get_array())
 
    def _start_spike(self):
 
        self.effects = []
        self.last_hue += self.hue_speed
        if self.last_hue > 1:
            self.last_hue -= 1
        rand_color = Colors.hls_to_rgb(self.last_hue, 1.0, 1.0)
        self.effects.append(AlwaysOnEffect(self.lake.waves_arr[self.last_wave], rand_color))

        contour_color = Colors.hls_to_rgb(self.last_hue, 0.5, 0.7)
        self.effects.append(AlwaysOnEffect(self.lake.contour, contour_color))
 
        self.last_wave += 1
        if self.last_wave >= len(self.lake.waves_arr):
            self.last_wave = 0
 
