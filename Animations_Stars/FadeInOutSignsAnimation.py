import math
import colorsys
from Colors import Colors
from Effects.FadeInEffect import FadeInEffect
from Effects.FadeOutEffect import FadeOutEffect

class FadeInOutSignsAnimation():

    def __init__(self, signs, num_of_spins, starting_hue):
        self.signs = signs
        self.num_of_spins = num_of_spins * 2
        self.current_spin = -1
        self.hue = starting_hue
    
    def apply(self, time_percent):
        spin = int(math.floor(time_percent * self.num_of_spins))
        if (spin != self.current_spin):
            self.current_spin = spin
            if (spin % 2 == 0):
                color = [int(c*255) for c in colorsys.hsv_to_rgb(self.hue, 1.0, 0.15)]
                self.effects = [FadeOutEffect(self.signs.get_all_indexes(), color)]
            else:
                self.hue = Colors.reduce_by_1(self.hue+0.29)
                color = [int(c*255) for c in colorsys.hsv_to_rgb(self.hue, 1.0, 0.15)]
                self.effects = [FadeInEffect(self.signs.get_all_indexes(), color)]

        oneSpinTime = 1.0 / float(self.num_of_spins)
        relativePercent = (time_percent - oneSpinTime * self.current_spin) * self.num_of_spins
        for effect in self.effects:
            effect.apply(relativePercent, self.signs.get_array())
