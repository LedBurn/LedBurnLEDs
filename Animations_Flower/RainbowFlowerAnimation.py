from FlowerAnimation import FlowerAnimation

from Effects.RainbowEffect import RainbowEffect
from Effects.GoToColorsEffect import GoToColorsEffect

from Colors import Colors

import random

class RainbowFlowerAnimation(FlowerAnimation):

    def __init__(self, flower, props):
        FlowerAnimation.__init__(self, flower, props)
        self.previous_time = 1;
        self.frame_counter = 0

    def createEffects(self):

        one = self.flower.l1 + self.flower.l3 + self.flower.l5 + self.flower.l7 + self.flower.l9
        two = self.flower.l8 + self.flower.l10 + self.flower.l2 + self.flower.l4 + self.flower.l6
        self.effects = []
        self.effects.append(RainbowEffect(one[::-1]))
        self.effects.append(RainbowEffect(two))

        seeds_order = self.flower.seeds[:]
        random.shuffle(seeds_order)
        self.effects.append(RainbowEffect(seeds_order))


        if self.frame_counter % 2 == 0:
            self.hue = random.random()
        color = Colors.hls_to_rgb(self.hue, 1, 1)
        light_color = [x*0.2 for x in color]

        gradient1_front = Colors.gradient_array(light_color, color, len(self.flower.line_front), 4)
        gradient2_front = Colors.gradient_array([30, 30, 30], [100, 100, 100],  len(self.flower.line_front), 4)
        gradient1_back = Colors.gradient_array(light_color, color, len(self.flower.line_back), 4)
        gradient2_back = Colors.gradient_array([30, 30, 30], [100, 100, 100], len(self.flower.line_back), 4)

        if self.frame_counter % 2 == 0:
            self.effects.append(GoToColorsEffect(self.flower.line_front ,gradient2_front, gradient1_front))
            self.effects.append(GoToColorsEffect(self.flower.line_back ,gradient2_back, gradient1_back))
        else: 
            self.effects.append(GoToColorsEffect(self.flower.line_front ,gradient1_front, gradient2_front))
            self.effects.append(GoToColorsEffect(self.flower.line_back ,gradient1_back, gradient2_back))

        gradient1_leaf1 = Colors.gradient_array(light_color, color, len(self.flower.leaf_right_front + self.flower.leaf_right_back), 4)
        gradient2_leaf1 = Colors.gradient_array([30, 30, 30], [100, 100, 100], len(self.flower.leaf_right_front + self.flower.leaf_right_back), 4)
        gradient1_leaf2 = Colors.gradient_array(light_color, color, len(self.flower.leaf_left_front + self.flower.leaf_left_back), 4)
        gradient2_leaf2 = Colors.gradient_array([30, 30, 30], [100, 100, 100], len(self.flower.leaf_left_front + self.flower.leaf_left_back), 4)

        if self.frame_counter % 2 == 0:
            self.effects.append(GoToColorsEffect(self.flower.leaf_right_front + self.flower.leaf_right_back ,gradient2_leaf1, gradient1_leaf1))
            self.effects.append(GoToColorsEffect(self.flower.leaf_left_front + self.flower.leaf_left_back ,gradient2_leaf2, gradient1_leaf2))
        else: 
            self.effects.append(GoToColorsEffect(self.flower.leaf_right_front + self.flower.leaf_right_back ,gradient1_leaf1, gradient2_leaf1))
            self.effects.append(GoToColorsEffect(self.flower.leaf_left_front + self.flower.leaf_left_back ,gradient1_leaf2, gradient2_leaf2))


    def apply(self, time_percent):
        
        if (time_percent < self.previous_time):
            self.createEffects()
            self.frame_counter += 1

        for effect in self.effects:
            effect.apply(time_percent, self.flower.get_array())

        self.previous_time = time_percent



