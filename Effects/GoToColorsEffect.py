import math
from AbstractEffect import Effect

import sys, os
sys.path.append(os.path.abspath('../Colors'))
from Colors import Colors

from GoToColorEffect import GoToColorEffect, GoToColorEffectType

class GoToColorsEffect(Effect):
    def __init__(self, indexes, from_colors, to_colors, type=GoToColorEffectType.CONST_SPEED):
        Effect.__init__(self, indexes)
        self.from_colors = from_colors
        self.to_colors = to_colors
        self.type = type
            
    
    def apply(self, time_precent, parent_array):
        
        power = time_precent
        if self.type == GoToColorEffectType.FAST_TO_SLOW:
            power = math.pow(time_precent, 0.25)
        elif self.type == GoToColorEffectType.SLOW_TO_FAST:
            power = math.pow(time_precent, 4)

        for i in range(len(self.indexes)):
            index = self.indexes[i]
            color = Colors().go_to_color(self.from_colors[i*3:i*3+3], self.to_colors[i*3:i*3+3], power)
            parent_array[index*3 : index*3+3] = color

    


