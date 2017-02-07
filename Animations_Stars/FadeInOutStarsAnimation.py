import math
import colorsys
import random
from Colors import Colors
from AbstractStarsAnimation import AbstractStarsAnimation
from Effects.FadeInEffect import FadeInEffect
from Effects.FadeOutEffect import FadeOutEffect
from Effects.StarShineEffect import StarShineEffect

class FadeInOutStarsAnimation(AbstractStarsAnimation):

    def __init__(self, stars, num_of_spins):
        AbstractStarsAnimation.__init__(self, stars)
        self.num_of_spins = max(num_of_spins / 2,1)
        self.current_spin = -1
        self.stars_to_apply = []
    
    def apply(self, time_percent):
        spin = int(math.floor(time_percent * self.num_of_spins))
        if (spin != self.current_spin):
            self.stars.clear()
            self.current_spin = spin
            self.stars_to_apply = [i for i in range(0, self.stars.num_of_stars()) if random.random() < 0.2]
            self.effects = [StarShineEffect([i], random.random()) for i in self.stars_to_apply]

        oneSpinTime = 1.0 / float(self.num_of_spins)
        relativePercent = (time_percent - oneSpinTime * self.current_spin) * self.num_of_spins
        for effect in self.effects:
            effect.apply(relativePercent, self.stars.get_array())
