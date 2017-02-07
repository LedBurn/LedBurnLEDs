import math
import colorsys
import random
from Colors import Colors
from AbstractSheepAnimation import SheepAnimation
from Effects.AlwaysOnEffect import AlwaysOnEffect
from Effects.FadeOutEffect import FadeOutEffect

class BrokenAnimation(SheepAnimation):

    def __init__(self, sheep, num_of_spins, num_of_lights):
        SheepAnimation.__init__(self, sheep)
        self.num_of_spins = num_of_spins * 2
        self.current_spin = -1
        self.num_of_lights = num_of_lights

        self.elements = [self.sheep.get_head_indexes(),
                         self.sheep.get_leg12_side1_indexes(),self.sheep.get_leg12_side2_indexes(),
                          self.sheep.get_leg34_side1_indexes(),self.sheep.get_leg34_side2_indexes()]
        if (len(self.sheep.get_inner_ear_indexes()) > 0):
            self.elements.append(self.sheep.get_inner_ear_indexes())
        if (len(self.sheep.get_outer_ear_indexes()) > 0):
            self.elements.append(self.sheep.get_outer_ear_indexes())
        for i in range(self.sheep.get_num_of_body_parts()):
            self.elements.append(self.sheep.get_body_part_indexes(i))
    
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
            effect.apply(relativePercent, self.sheep.get_array())
