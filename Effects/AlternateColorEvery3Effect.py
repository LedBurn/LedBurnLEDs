from AbstractEffect import Effect

import math

class AlternateColorEvery3Effect(Effect):
    
    def __init__(self, indexes, color1, color2):
        Effect.__init__(self, indexes)
        self.color1 = color1
        self.color2 = color2
    
    def apply(self, time_precent, parent_array):

        #switch 8 times until 1
        is1onOn1 = int(math.floor(time_precent  * 4.0)) % 2 == 0

        for i in range(len(self.indexes)):
            if (is1onOn1):
                if ((i/3)%2==0):
                    parent_array[self.indexes[i]*3 : self.indexes[i]*3+3] = self.color1
                else:
                    parent_array[self.indexes[i]*3 : self.indexes[i]*3+3] = self.color2
            else:
                if ((i/3)%2==0):
                    parent_array[self.indexes[i]*3 : self.indexes[i]*3+3] = self.color2
                else:
                    parent_array[self.indexes[i]*3 : self.indexes[i]*3+3] = self.color1
