from FlowerAnimation import FlowerAnimation

import sys, os
sys.path.append(os.path.abspath('../Effects'))
from GoToColorEffect import GoToColorEffect, GoToColorEffectType
from AdvanceEffect import AdvanceEffect
from AlwaysOnEffect import AlwaysOnEffect

sys.path.append(os.path.abspath('../Colors'))
from Colors import Colors

import random

class ExplosionFlowerAnimation(FlowerAnimation):

    def __init__(self, flower):
        FlowerAnimation.__init__(self, flower)
        self.previous_time = 1;
        self.frame_counter = 0
        self.color = [0, 0, 0]
        self.previous_color = [0, 0, 0]
        self.effects = []

    def create_bottom_animation(self):
        self.effects = []

        self.previous_color = self.color
        hue = random.random()
        self.color = Colors().hls_to_rgb(hue, 1 ,1 )

        self.effects.append(AdvanceEffect.initColor(self.flower.line_back, self.previous_color, self.color))
        self.effects.append(AdvanceEffect.initColor(self.flower.line_front, self.previous_color, self.color))
        self.effects.append(AdvanceEffect.initColor(self.flower.leaf_right_front, self.previous_color, self.color))
        self.effects.append(AdvanceEffect.initColor(self.flower.leaf_right_back, self.previous_color, self.color))
        self.effects.append(AdvanceEffect.initColor(self.flower.leaf_left_front, self.previous_color, self.color))
        self.effects.append(AdvanceEffect.initColor(self.flower.leaf_left_back, self.previous_color, self.color))

        self.effects.append(AlwaysOnEffect(self.flower.seeds, self.previous_color))
        self.effects.append(AlwaysOnEffect(self.flower.get_leaves(), self.previous_color))


    def create_seeds_animation(self):

        self.effects = []
        self.effects.append(GoToColorEffect(self.flower.seeds, self.previous_color, self.color)) 

        self.effects.append(AlwaysOnEffect(self.flower.bottom_parts, self.color))
        self.effects.append(AlwaysOnEffect(self.flower.get_leaves(), self.previous_color))

    def create_last_animation(self):
        self.effects = []

        for leaf in self.flower.get_leaves_array():
            leaf_1 = leaf[:len(leaf)/2]
            leaf_2 = leaf[len(leaf)/2:][::-1]
            self.effects.append(AdvanceEffect.initColor(leaf_1, self.previous_color, self.color))
            self.effects.append(AdvanceEffect.initColor(leaf_2, self.previous_color, self.color))

        self.effects.append(AlwaysOnEffect(self.flower.bottom_parts, self.color))
        self.effects.append(AlwaysOnEffect(self.flower.seeds, self.color))

    def apply(self, time_percent):

        if (time_percent < self.previous_time):
            self.effects = []

            if self.frame_counter % 4 == 0:
                self.create_bottom_animation()

            if self.frame_counter % 4 == 1:
                self.create_seeds_animation()

            if self.frame_counter % 4 == 2:
                self.create_last_animation()

            if self.frame_counter % 4 == 3:
                self.effects.append(AlwaysOnEffect(self.flower.bottom_parts, self.color))
                self.effects.append(AlwaysOnEffect(self.flower.seeds, self.color)) 
                self.effects.append(AlwaysOnEffect(self.flower.get_leaves(), self.color))

            self.frame_counter += 1

        for effect in self.effects:
            effect.apply(time_percent, self.flower.get_array())

        self.previous_time = time_percent



