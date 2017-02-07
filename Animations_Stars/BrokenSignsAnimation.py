import math
import colorsys
import random
from Colors import Colors
from UIElements.Signs import Signs
from Effects.AlwaysOnEffect import AlwaysOnEffect
from Effects.FadeOutEffect import FadeOutEffect

class BrokenSignsAnimation():

    def __init__(self, signs, num_of_spins, num_of_lights):
        self.signs = signs
        self.num_of_spins = num_of_spins * 2
        self.current_spin = -1
        self.num_of_lights = num_of_lights

        self.elements = signs.get_letters()
        self.hues = [0] * len(self.elements)
        for i in range(len(self.elements)):
            self.hues[i] = random.random()
    
    def apply(self, time_percent):
        spin = int(math.floor(time_percent * self.num_of_spins))
        if (spin != self.current_spin):
            self.current_spin = spin
            on = []
            for i in range(self.num_of_lights):
                on.append(random.randrange(len(self.elements)))
            
            self.effects = []
            for i in range(len(self.elements)):
                hue = self.hues[i]
                color = [int(c*255) for c in colorsys.hsv_to_rgb(hue, 1.0, 0.03)]
                self.effects.append(AlwaysOnEffect(self.elements[i], color))

            for i in range(len(on)):
                hue = self.hues[on[i]]
                color = [int(c*255) for c in colorsys.hsv_to_rgb(hue, 1.0, 0.35)]
                to_color = [int(c*255) for c in colorsys.hsv_to_rgb(hue, 1.0, 0.03)]
                self.effects.append(FadeOutEffect.initLimit(self.elements[on[i]], color, to_color,1))    

        oneSpinTime = 1.0 / float(self.num_of_spins)
        relativePercent = (time_percent - oneSpinTime * self.current_spin) * self.num_of_spins
        for effect in self.effects:
            effect.apply(relativePercent, self.signs.get_array())
