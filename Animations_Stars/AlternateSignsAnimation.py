import math
import colorsys
from Colors import Colors

from UIElements.Signs import Signs
from Effects.AlternateColorEvery3Effect import AlternateColorEvery3Effect

class AlternateSignsAnimation():

    def __init__(self, signs, num_of_spins, starting_hue):
        self.signs = signs
        self.num_of_spins = num_of_spins
        self.current_spin = -1
        self.hue1 = starting_hue
    
    def apply(self, time_percent):
        spin = int(math.floor(time_percent * self.num_of_spins))
        if (spin != self.current_spin):
            self.current_spin = spin
            self.hue1 = Colors.reduce_by_1(self.hue1 + 0.4)
            self.hue2 = Colors.reduce_by_1(self.hue1+0.25)
            self.current_color1 = [int(c*255) for c in colorsys.hsv_to_rgb(self.hue1, 1.0, 0.15)]
            self.current_color2 = [int(c*255) for c in colorsys.hsv_to_rgb(self.hue2, 1.0, 0.15)]
            self.effect = AlternateColorEvery3Effect(self.signs.get_all_indexes(),self.current_color1,self.current_color2)

        oneSpinTime = 1.0 / self.num_of_spins
        relativePercent = (time_percent - oneSpinTime * self.current_spin) * self.num_of_spins
        self.effect.apply(relativePercent, self.signs.get_array())
