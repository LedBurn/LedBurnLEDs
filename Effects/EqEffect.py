from AbstractEffect import Effect

import colorsys
import random


class EqEffect(Effect):
    def __init__(self, indexes, leds_percent_per_beat, brightness=1.0):
        Effect.__init__(self, indexes)
        self.hue = 0
        self.eq_start = random.uniform(0.2, 0.7)
        self.curr_pos = self.eq_start
        self.last_time_percent = 0

    def _global_value(self, time_percent):
        if time_percent < 0.05 or time_percent > 0.95:
            return 1.0
        elif time_percent < 0.3:
            return (0.3 - time_percent) / (0.3-0.05)
        else:
            return (time_percent - 0.3) / (0.95-0.3)

    def apply(self, time_percent, parent_array):

        self.hue = (self.hue + 1.0 / 180.0)
        if time_percent < self.last_time_percent:
            self.eq_start = random.uniform(0.2, 0.7)
        self.last_time_percent = time_percent

        percent = (self.eq_start + random.uniform(-0.00, 0.00)) + ( (self._global_value(time_percent) - 0.2) * 0.5)
        percent = max(percent, 0.0)
        percent = min(percent, 1.0)
        self.curr_pos = self.curr_pos + (percent - self.curr_pos) * 0.4
        v = int(len(self.indexes) * self.curr_pos)

        """ fade to black """
        for i in range(0, v):
            obj_pixel = self.indexes[i]
            parent_array[3 * obj_pixel: 3 * obj_pixel + 3] = [0, 0, 255]
        for i in range(v, len(self.indexes)):
            obj_pixel = self.indexes[i]
            parent_array[3 * obj_pixel: 3 * obj_pixel + 3] = [0, 255, 0]
