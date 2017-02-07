import math
from AbstractEffect import Effect

class BlinkEffect(Effect):
    def __init__(self, indexes, num_of_blinks, color):
        Effect.__init__(self, indexes)
        self.num_of_blinks = num_of_blinks
        self.color = color
    
    def apply(self, time_percent, parent_array):
        for i in self.indexes:
            blinkNumber = int(math.floor(time_percent * self.num_of_blinks))
            relativePercent = (time_percent - (1.0 / self.num_of_blinks * blinkNumber)) * self.num_of_blinks
            if (relativePercent < 0.25):
                parent_array[i*3 : i*3+3] = self.color
            else:
                parent_array[i*3 : i*3+3] = [0,0,0]


