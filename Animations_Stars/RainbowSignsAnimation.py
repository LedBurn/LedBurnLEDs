import math
from Colors import Colors

from UIElements.Signs import Signs
from Effects.RainbowEffect import RainbowEffect


class RainbowSignsAnimation():

    def __init__(self, signs, num_of_spins):
        self.signs = signs
        self.num_of_spins = num_of_spins
        self.current_spin = -1
        self.effect = RainbowEffect(self.signs.get_all_indexes()[::-1])
    
    def apply(self, time_percent):
        spin = int(math.floor(time_percent * self.num_of_spins))
        if (spin != self.current_spin):
            self.current_spin = spin

        oneSpinTime = 1.0 / self.num_of_spins
        relativePercent = (time_percent - oneSpinTime * self.current_spin) * self.num_of_spins
        self.effect.apply(relativePercent, self.signs.get_array())
