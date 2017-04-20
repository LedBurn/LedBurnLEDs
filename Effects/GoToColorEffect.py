import math
from AbstractEffect import Effect

from Colors import Colors

class GoToColorEffectType:
    CONST_SPEED = 0
    FAST_TO_SLOW = 1
    SLOW_TO_FAST = 2

class GoToColorEffect(Effect):
    def __init__(self, indexes, from_color, to_color, type=GoToColorEffectType.CONST_SPEED):
        Effect.__init__(self, indexes)
        self.from_color = from_color
        self.to_color = to_color
        self.type = type
            
    
    def apply(self, time_precent, parent_array):
        
        power = time_precent
        if self.type == GoToColorEffectType.FAST_TO_SLOW:
            power = math.pow(time_precent, 0.25)
        elif self.type == GoToColorEffectType.SLOW_TO_FAST:
            power = math.pow(time_precent, 4)

        color = Colors.go_to_color(self.from_color, self.to_color, power)

        for i in self.indexes:
            parent_array[i*3 : i*3+3] = color

    


