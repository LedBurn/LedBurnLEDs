from FlowerAnimation import FlowerAnimation

from Effects.FireEffect import FireEffect
from Effects.AlwaysOnEffect import AlwaysOnEffect

import random

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

        # for col in self.flower.bottom_to_top_cols:
        #     self.effects.append(FireEffect(col))

        for leaf in self.flower.top_leaves_arr:
            # split to 2 chunks
            size = len(leaf)/2
            arr = [leaf[i:i + size] for i in xrange(0, len(leaf), size)]
            up = arr[0]
            down = arr[1]

            self.effects.append(FireEffect(up))
            self.effects.append(FireEffect(down[::-1]))
        
        self.effects.append(AlwaysOnEffect(self.flower.seeds, [200, 0, 0]))
        # self.seedsEffect = FireEffect(self.flower.seeds)

    def apply(self, time_percent):
        
        for effect in self.effects:
            effect.apply(time_percent, self.flower.get_array())

        # self.seedsEffect.apply(time_percent, self.flower.get_array())

        # colors = [self.flower.get_array()[seed*3: seed*3+3] for seed in self.flower.seeds]
        # random.shuffle(colors)

        # for i in range(len(self.flower.seeds)):
        #     self.flower.get_array()[self.flower.seeds[i]*3: self.flower.seeds[i]*3+3] = colors[i]


