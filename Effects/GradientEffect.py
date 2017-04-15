import math
from AbstractEffect import Effect

import sys, os
sys.path.append(os.path.abspath('../Colors'))
from Colors import Colors 

class GradientEffect(Effect):
    def __init__(self, indexes, from_color, to_color, power=1):
        Effect.__init__(self, indexes)
        self.from_color = from_color
        self.to_color = to_color
        self.power = power
    
    def apply(self, time_percent, parent_array):
        for i in range(len(self.indexes)):
            index = self.indexes[i]
            percent = float(i) / len(self.indexes)
            percent = math.pow(percent, self.power)
            color = Colors.Colors().go_to_color(self.from_color, self.to_color, percent)
            parent_array[index*3 : index*3+3] = color


