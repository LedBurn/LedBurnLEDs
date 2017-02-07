from AbstractEffect import Effect

import math

class AlternateColor2ArraysEffect(Effect):
    
    def __init__(self, indexes, indexes2, color1, color2):
        Effect.__init__(self, indexes)
        self.indexes2 = indexes2
        self.color1 = color1
        self.color2 = color2
    
    def apply(self, time_precent, parent_array):

        #switch 4 times until 1
        is1onOn1 = int(math.floor(time_precent  * 4.0)) % 2 == 0

        for i in self.indexes:
            if (is1onOn1):
                parent_array[i*3 : i*3+3] = self.color1
            else:
                parent_array[i*3 : i*3+3] = self.color2

        for i in self.indexes2:
            if (is1onOn1):
                parent_array[i*3 : i*3+3] = self.color2
            else:
                parent_array[i*3 : i*3+3] = self.color1
