from AbstractEffect import Effect

import colorsys
import random

class ConfettiEffect(Effect):
    def __init__(self, indexes, leds_percent_per_beat, brightness=1.0, fade_factor=0.9):
        Effect.__init__(self, indexes)
        self.hue = 0
        self.fade_factor = fade_factor

        self.brightness = brightness
        self.number_of_leds_per_beat = int(leds_percent_per_beat * len(self.indexes))
        self.lighted_counter = 0
    
    def apply(self, time_percent, parent_array):
        
        self.hue = (self.hue + 1.0/180.0)
        if self.hue > 1.0:
            self.hue -= 1
            
        """ fade to black """
        for i in self.indexes:
            parent_array[3*i] = int(parent_array[3*i] * self.fade_factor)
            parent_array[3*i+1] = int(parent_array[3*i+1] * self.fade_factor)
            parent_array[3*i+2] = int(parent_array[3*i+2] * self.fade_factor)
        
        """ add new full light color pixels """
        curr_lighted_percent = float(self.lighted_counter)/self.number_of_leds_per_beat
        diff = (time_percent - curr_lighted_percent) % 1
        new_counter = int(diff * self.number_of_leds_per_beat)
        self.lighted_counter += new_counter

        for _ in range(new_counter):
            rand_pixel = self.indexes[random.randint(0, len(self.indexes) - 1)]
            rand_index = rand_pixel * 3
            parent_array[rand_index : rand_index+3] = [int(c*255) for c in colorsys.hsv_to_rgb(self.hue + random.random() / 10, 0.75, self.brightness)]
