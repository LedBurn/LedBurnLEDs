import math
import colorsys
from Colors import Colors
from AbstractSheepAnimation import SheepAnimation
from Effects.AlwaysOnEffect import AlwaysOnEffect
from Effects.SpinningFadeEffect import SpinningFadeEffect
from Effects.AlternateColorEffect import AlternateColorEffect
from Effects.AdvanceEffect import AdvanceEffect

class SpinningHeadAnimation(SheepAnimation):

    def __init__(self, sheep, hue, num_of_spins):
        SheepAnimation.__init__(self, sheep)
        self.num_of_spins = num_of_spins
        self.current_spin = -1
        self.color = [int(c*255) for c in colorsys.hsv_to_rgb(hue, 1.0, 0.25)]
        hue2 = Colors.reduce_by_1(hue+0.5)
        self.headColor = [int(c*255) for c in colorsys.hsv_to_rgb(hue2, 1.0, 0.25)]
        
        self.legsColor1 = self.color#Colors.adjacent_color(self.color)[0]
        self.legsColor2 = self.headColor#Colors.adjacent_color(self.color)[1]
        
    def create_effects(self):
        bodyEffect = SpinningFadeEffect(self.sheep.get_body_indexes, self.color)

        head_indexes = self.sheep.get_head_indexes()[::-1]
        headEffect = SpinningFadeEffect(head_indexes,self.headColor)
        
        #legsEffect = AlternateColorEffect(self.sheep.get_legs_indexes(), self.legsColor1, self.legsColor2)
        #earlEffect = AdvanceEffect.initSpin(self.sheep.earl, self.current_spin)
        #earrEffect = AdvanceEffect.initSpin(self.sheep.earr, self.current_spin)
        self.effects = [bodyEffect, headEffect]
    
    def apply(self, time_percent):
        spin = int(math.floor(time_percent * self.num_of_spins))
        if (spin != self.current_spin):
            self.current_spin = spin;
            self.create_effects()

        oneSpinTime = 1.0 / self.num_of_spins
        relativePercent = (time_percent - oneSpinTime * self.current_spin) * self.num_of_spins
        for effect in self.effects:
            effect.apply(relativePercent, self.sheep.get_array())
