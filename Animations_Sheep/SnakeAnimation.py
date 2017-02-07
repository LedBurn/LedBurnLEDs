from AbstractSheepAnimation import SheepAnimation
from Effects.FadingSnakeEffect import FadingSnakeEffect
from Effects.ConfettiEffect import ConfettiEffect

import math
import random

class SnakeAnimation(SheepAnimation):
    def __init__(self, sheep, num_of_spins):
        SheepAnimation.__init__(self, sheep)
        self.num_of_spins = num_of_spins
        self.effects = [
            ConfettiEffect(self.sheep.get_head_indexes() + self.sheep.get_legs_indexes() + self.sheep.get_ears_indexes(), 1),
            FadingSnakeEffect(self.sheep.get_body_indexes(), 1),
            ]
    
    def apply(self, time_percent):
        spin = int(math.floor(time_percent * self.num_of_spins))
        oneSpinTime = 1.0 / float(self.num_of_spins)
        relativePercent = (time_percent - oneSpinTime * spin) * self.num_of_spins
        for effect in self.effects:
            effect.apply(relativePercent, self.sheep.get_array())
        
