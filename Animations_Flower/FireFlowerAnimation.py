from FlowerAnimation import FlowerAnimation

import sys, os
sys.path.append(os.path.abspath('../UIElements'))
from Sign import Sign

sys.path.append(os.path.abspath('../Effects'))
from FireEffect import FireEffect
from AlwaysOnEffect import AlwaysOnEffect

class FireFlowerAnimation(FlowerAnimation):

    def __init__(self, flower, props):
        FlowerAnimation.__init__(self, flower, props)

        self.effects = []
        self.effects.append(FireEffect(self.flower.line_front))
        self.effects.append(FireEffect(self.flower.line_back))
        self.effects.append(FireEffect(self.flower.leaf_right_front))
        self.effects.append(FireEffect(self.flower.leaf_right_back))
        self.effects.append(FireEffect(self.flower.leaf_left_front))
        self.effects.append(FireEffect(self.flower.leaf_left_back))

        for col in self.flower.bottom_to_top_cols:
            self.effects.append(FireEffect(col))

    def apply(self, time_percent):
        
        for effect in self.effects:
            effect.apply(time_percent, self.flower.get_array())



