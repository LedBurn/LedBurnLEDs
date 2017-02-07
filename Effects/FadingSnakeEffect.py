from AbstractEffect import Effect

import colorsys
import random
import math

class FadingSnakeEffect(Effect):
    def __init__(self, indexes, number_of_snakes):
        Effect.__init__(self, indexes)
        self._number_of_snakes = number_of_snakes
        self.hue_start = random.random()
        self.start_pos = 0
    
    def apply(self, time_precent, parent_array):
        if len(self.indexes) == 0:
            return
            
        curr_snake_pos = int(time_precent * len(self.indexes))
        
        self.hue_start = self.hue_start + 0.01
        while self.hue_start > 1.0:
            self.hue_start = self.hue_start - 1.0
        while self.hue_start < 0.0:
            self.hue_start = self.hue_start + 1.0
        
        """ fade to black """
        for i in self.indexes:
            parent_array[3*i] = int(parent_array[3*i] * 0.87)
            parent_array[3*i+1] = int(parent_array[3*i+1] * 0.9)
            parent_array[3*i+2] = int(parent_array[3*i+2] * 0.9)
        
        """ add new full light color pixels """
        for i in range(0, self._number_of_snakes):
            pix = self.indexes[curr_snake_pos % len(self.indexes)]
            parent_array[pix * 3 : (pix + 1) * 3] = [int(c*255) for c in colorsys.hsv_to_rgb(self.hue_start, 0.8, 1.0)]
            
        self.start_pos = (self.start_pos + 1) % len(self.indexes)
