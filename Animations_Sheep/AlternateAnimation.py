import math
import colorsys
from Colors import Colors
from AbstractSheepAnimation import SheepAnimation
from Effects.AlternateColorEvery3Effect import AlternateColorEvery3Effect
from Effects.AlternateColor2ArraysEffect import AlternateColor2ArraysEffect
from Effects.AlwaysOnEffect import AlwaysOnEffect
from Effects.AdvanceEffect import AdvanceEffect

class AlternateAnimation(SheepAnimation):

    def __init__(self, sheep, num_of_spins, starting_hue):
        SheepAnimation.__init__(self, sheep)
        self.num_of_spins = num_of_spins
        self.current_spin = -1
        self.hue1 = starting_hue
        
    def create_effects(self):
        bodyEffect = AlternateColorEvery3Effect(self.sheep.get_body_indexes(),self.current_color1,self.current_color2)
        
        #leg12Effect = AlternateColor2ArraysEffect(self.sheep.get_leg12_side1_indexes(),self.sheep.get_leg12_side2_indexes() ,self.current_color1,self.current_color2)
        #leg34Effect = AlternateColor2ArraysEffect(self.sheep.get_leg34_side1_indexes(),self.sheep.get_leg34_side2_indexes() ,self.current_color1,self.current_color2)
        legsEffect1 = AlwaysOnEffect(self.sheep.get_leg12_side1_indexes() + self.sheep.get_leg34_side1_indexes(), self.current_color2)
        legsEffect2 = AlwaysOnEffect(self.sheep.get_leg12_side2_indexes() + self.sheep.get_leg34_side2_indexes(), self.current_color1)

        headEffect = AlwaysOnEffect(self.sheep.get_head_indexes(),self.current_color1)
        earsEffect1 = AdvanceEffect.initColor(self.sheep.get_inner_ear_indexes()[::-1], self.current_color2, self.current_color1)
        earsEffect2 = AdvanceEffect.initColor(self.sheep.get_outer_ear_indexes()[::-1], self.current_color2, self.current_color1)
      
        self.effects = [bodyEffect, legsEffect1, legsEffect2, headEffect, earsEffect1, earsEffect2]
    
    def apply(self, time_percent):
        spin = int(math.floor(time_percent * self.num_of_spins))
        if (spin != self.current_spin):
            self.current_spin = spin
            self.hue1 = Colors.reduce_by_1(self.hue1 + 0.4)
            self.hue2 = Colors.reduce_by_1(self.hue1+0.25)
            self.current_color1 = [int(c*255) for c in colorsys.hsv_to_rgb(self.hue1, 0.8, 0.8)]
            self.current_color2 = [int(c*255) for c in colorsys.hsv_to_rgb(self.hue2, 0.8, 0.8)]
            self.create_effects()

        oneSpinTime = 1.0 / self.num_of_spins
        relativePercent = (time_percent - oneSpinTime * self.current_spin) * self.num_of_spins
        for effect in self.effects:
            effect.apply(relativePercent, self.sheep.get_array())
