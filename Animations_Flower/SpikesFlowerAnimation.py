from FlowerAnimation import FlowerAnimation

from UIElements.Flower import Flower

from Effects.SpikeEffect import SpikeEffect
from Effects.FadeInOutEffect import FadeInOutEffect

from Colors import Colors
from Colors.TimedColor import TimedColorFactory, ConstTimedColor, HueChangeTimedColor, CircularLocHue

import random

class SpikesFlowerAnimation(FlowerAnimation):

    def __init__(self, flower, props):
        FlowerAnimation.__init__(self, flower, props)
        self.effects = []
        self.previous_time = 1

        self.effects = []
        self.color = HueChangeTimedColor(0.0, 1.0)

        self.include_seeds = True

        self.hue_speed = 0.03125
        self.hue = random.random()
        if self.props != None:
            if 'include_seeds' in self.props:
                self.include_seeds = self.props['include_seeds']
            if 'color' in self.props:
                self.color = TimedColorFactory(self.props['color'])


    def apply(self, time_percent):

        if time_percent < self.previous_time:
            self.create_spike()
        self.previous_time = time_percent

        for effect in self.effects:
            effect.apply(time_percent, self.flower.get_array())

    def create_spike(self):
        self.effects = []

        if self.include_seeds:
            self.effects.append(FadeInOutEffect(self.flower.get_seeds(), self.color))
        for leaf in self.flower.get_leaves_array():
            self.effects.append(SpikeEffect(leaf, self.color, 0.5, len(leaf)))
        self.effects.append(SpikeEffect(self.flower.get_left_leaf(), self.color, 0.5, len(self.flower.get_left_leaf())))
        self.effects.append(SpikeEffect(self.flower.get_right_leaf(), self.color, 0.5, len(self.flower.get_right_leaf())))



