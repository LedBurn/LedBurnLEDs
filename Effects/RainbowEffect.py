from AbstractEffect import Effect

import colorsys

class RainbowEffect(Effect):
    
    def __init__(self, indexes):
        Effect.__init__(self, indexes)
   
    def apply(self, time_precent, parent_array):

        for i in range(len(self.indexes)):
            hue = i / float(len(self.indexes)) + time_precent
            if (hue >= 1):
                hue -= 1
            parent_array[self.indexes[i]*3 : self.indexes[i]*3+3] = [int(c*255) for c in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
