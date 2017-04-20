from FlowerAnimation import FlowerAnimation

from UIElements.Flower import Flower

from Effects.GoToColorEffect import GoToColorEffect
from Effects.AlwaysOnEffect import AlwaysOnEffect

from Colors import Colors

import random

class NaturalFlowerAnimation(FlowerAnimation):

    def __init__(self, flower, props):
        FlowerAnimation.__init__(self, flower, props)
        self.effects = []
        self.previous_time = 1

        self.hue_speed = 0.03125
        self.hue = random.random()
        if self.props != None:
            if 'hue_speed' in self.props:
                self.hue_speed = self.props['hue_speed']
            if 'hue_start' in self.props:
                self.hue = self.props['hue_start']


    def apply(self, time_percent):

        if time_percent < self.previous_time:
            self.next_hue()
        self.previous_time = time_percent

        for effect in self.effects:
            effect.apply(time_percent, self.flower.get_array())

    def next_hue(self):
        self.effects = []

        new_hue = self.hue + self.hue_speed
        if new_hue > 1 : new_hue -= 1
        prev_color = Colors.hls_to_rgb(self.hue, 1.0, 1.0)
        new_color = Colors.hls_to_rgb(new_hue, 1.0, 1.0)
        self.effects.append(GoToColorEffect(self.flower.get_leaves() + self.flower.seeds, prev_color, new_color))
        self.hue = new_hue

        self.effects.append(AlwaysOnEffect(self.flower.line, [50, 200, 0]))
        self.effects.append(AlwaysOnEffect(self.flower.leaves, [0, 200, 0]))






