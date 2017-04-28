from AbstractEffect import Effect

from Colors import Colors
import random


class EqEffect(Effect):
    def __init__(self, indexes, brightness=1.0, hue1 = 0.6, hue2 = 0.8):
        Effect.__init__(self, indexes)
        self.brightness = brightness
        self.hue1 = hue1
        self.hue2 = hue2
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

        if time_percent < self.last_time_percent:
            self.eq_start = random.uniform(0.2, 0.7)
        self.last_time_percent = time_percent

        percent = (self.eq_start + random.uniform(-0.00, 0.00)) + ( (self._global_value(time_percent) - 0.2) * 0.5)
        percent = max(percent, 0.0)
        percent = min(percent, 1.0)
        self.curr_pos = self.curr_pos + min((percent - self.curr_pos) * 0.4, int(len(self.indexes) * 0.03))
        v = int(len(self.indexes) * self.curr_pos)

        """ fade to black """
        for i in range(0, v):
            obj_pixel = self.indexes[i]
            parent_array[3 * obj_pixel: 3 * obj_pixel + 3] = Colors.hls_to_rgb(self.hue1, 1.0, self.brightness)
        for i in range(v, len(self.indexes)):
            obj_pixel = self.indexes[i]
            parent_array[3 * obj_pixel: 3 * obj_pixel + 3] = Colors.hls_to_rgb(self.hue2, 1.0, self.brightness)
