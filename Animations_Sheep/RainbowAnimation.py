import math
from Colors import Colors
from AbstractSheepAnimation import SheepAnimation
from Effects.RainbowEffect import RainbowEffect
from Effects.AlwaysOnEffect import AlwaysOnEffect

class RainbowAnimation(SheepAnimation):

    def __init__(self, sheep, num_of_spins):
        SheepAnimation.__init__(self, sheep)
        self.num_of_spins = num_of_spins
        self.current_spin = -1
        self.create_effects()
        
    def create_effects(self):
        bodyEffect = RainbowEffect(self.sheep.get_body_indexes())
        headEffect = RainbowEffect(self.sheep.get_head_indexes())
        self.effects = [bodyEffect, headEffect]
    
    def apply(self, time_percent):
        spin = int(math.floor(time_percent * self.num_of_spins))
        if (spin != self.current_spin):
            self.current_spin = spin

        oneSpinTime = 1.0 / self.num_of_spins
        relativePercent = (time_percent - oneSpinTime * self.current_spin) * self.num_of_spins
        for effect in self.effects:
            effect.apply(relativePercent, self.sheep.get_array())

        leg12color = self.sheep.get_array()[self.sheep.get_leg12_connection_index()*3 :
                                            self.sheep.get_leg12_connection_index()*3 + 3]
        legs12Effect = AlwaysOnEffect(self.sheep.get_leg12_indexes(), leg12color)
        legs12Effect.apply(time_percent, self.sheep.get_array())

        leg34color = self.sheep.get_array()[self.sheep.get_leg34_connection_index()*3 :
                                            self.sheep.get_leg34_connection_index()*3 + 3]
        legs34Effect = AlwaysOnEffect(self.sheep.get_leg34_indexes(), leg34color)
        legs34Effect.apply(time_percent, self.sheep.get_array())

        inner_ear_color = self.sheep.get_array()[self.sheep.get_inner_ear_connection_index()*3 :
                                            self.sheep.get_inner_ear_connection_index()*3 + 3]
        inner_ear_effect = AlwaysOnEffect(self.sheep.get_inner_ear_indexes(), inner_ear_color)
        inner_ear_effect.apply(time_percent, self.sheep.get_array())

        outer_ear_color = self.sheep.get_array()[self.sheep.get_outer_ear_connection_index()*3 :
                                            self.sheep.get_outer_ear_connection_index()*3 + 3]
        outer_ear_effect = AlwaysOnEffect(self.sheep.get_outer_ear_indexes(), outer_ear_color)
        outer_ear_effect.apply(time_percent, self.sheep.get_array())
