from AbstractEffect import Effect

import colorsys
import random

class ConfettiEffect(Effect):
    def __init__(self, indexes, leds_percent_per_cycle):
        Effect.__init__(self, indexes)
        self._leds_per_cycle = int(leds_percent_per_cycle * len(self.indexes))
        self.hue = 0
    
    def apply(self, time_precent, parent_array):
        
        self.hue = (self.hue + 1.0/180.0)
        if self.hue > 1.0:
            self.hue = 0
            
        """ fade to black """
        for i in self.indexes:
            parent_array[3*i] = int(parent_array[3*i] * 0.9)
            parent_array[3*i+1] = int(parent_array[3*i+1] * 0.9)
            parent_array[3*i+2] = int(parent_array[3*i+2] * 0.9)
        
        """ add new full light color pixels """
        for _ in range(0, self._leds_per_cycle):
            rand_pixel = self.indexes[random.randint(0, len(self.indexes) - 1)]
            rand_index = rand_pixel * 3
            parent_array[rand_index : rand_index+3] = [int(c*255) for c in colorsys.hsv_to_rgb(self.hue + random.random() / 10, 0.75, 1.0)]
