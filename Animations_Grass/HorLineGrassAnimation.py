from GrassAnimation import GrassAnimation

import sys, os
sys.path.append(os.path.abspath('../Effects'))
from SinglePixelEffect import SinglePixelEffect


sys.path.append(os.path.abspath('../Colors'))
from Colors import Colors

import random, colorsys

class HorLineGrassAnimation(GrassAnimation):

    def __init__(self, grass, props):
        GrassAnimation.__init__(self, grass, props)
        self.effects = []

        self.on_time_percent = 0.5
        self.hue = 0.33
        self.pixel_hue = 0.7
        if self.props != None:
            if 'on_time_percent' in self.props:
                self.on_time_percent = self.props['on_time_percent']
            if 'hue_start' in self.props:
                self.hue = self.props['hue_start']
            if 'pixel_hue' in self.props:
                self.pixel_hue = self.props['pixel_hue']


        max_height = 0
        for leaf in self.grass.get_leaves_array():
            max_height = max(max_height, len(leaf[0]))
            max_height = max(max_height, len(leaf[1]))

        for leaf in self.grass.get_leaves_array():
            rand_leaf_color = Colors.hls_to_rgb(self.hue, random.uniform(0.35, 1), random.uniform(0.35, 1))
            pixel_color = Colors.hls_to_rgb(self.pixel_hue, 1.0, 1.0)
            self.effects.append(SinglePixelEffect(leaf[0], rand_leaf_color, pixel_color, max_height * (1 + self.on_time_percent)))
            self.effects.append(SinglePixelEffect(leaf[1][::-1], rand_leaf_color, pixel_color, max_height * (1 + self.on_time_percent)))

    def apply(self, time_percent):

        for effect in self.effects:
            effect.apply(time_percent, self.grass.get_array())



