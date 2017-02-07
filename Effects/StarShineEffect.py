from AbstractEffect import Effect

import colorsys
import random
import math

class StarShineEffect(Effect):
    
    def __init__(self, indexes, hue):
        Effect.__init__(self, indexes)
        self._start_percent = random.random() * 0.2
        self._full_percent = self._start_percent + max(0.1, random.random() * 0.3)
        self._stop_percent = 1.0 - random.random() * 0.2
        self._decent_percent = self._stop_percent - max(0.1, random.random() * 0.3)
        self.hue = hue
        self.max_brightness = 0.5 * random.random()
   
    def apply(self, time_precent, parent_array):

        brightness = 0
        if time_precent < self._start_percent:
            brightness = 0
        elif time_precent < self._full_percent:
            brightness = float(time_precent) / self._full_percent
        elif time_precent < self._decent_percent:
            brightness = 1.0 - random.random() * 0.3
        elif time_precent < self._stop_percent:
            brightness = (self._stop_percent - time_precent) / (self._stop_percent - self._decent_percent)
        else:
            brightness = 0
        brightness = math.pow(brightness,1)
        brightness = self.max_brightness * brightness
    
        for i in range(len(self.indexes)):
            parent_array[self.indexes[i]*3 : self.indexes[i]*3+3] = [int(c*255) for c in colorsys.hsv_to_rgb(self.hue, 0.45, brightness)]
