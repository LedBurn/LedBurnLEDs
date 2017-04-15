from GrassAnimation import GrassAnimation

import sys, os
sys.path.append(os.path.abspath('../UIElements'))
from Grass import Grass

sys.path.append(os.path.abspath('../Effects'))
from FireEffect import FireEffect

class FireGrassAnimation(GrassAnimation):

    def __init__(self, grass):
        GrassAnimation.__init__(self, grass)
        
        self.effects = []
        for leaf in self.grass.get_leaves_array():
            up = leaf[0]
            down = leaf[1][::-1]
            self.effects.append(FireEffect(up))
            self.effects.append(FireEffect(down))
    

    def apply(self, time_percent):
        
        for effect in self.effects:
            effect.apply(time_percent, self.grass.get_array())






