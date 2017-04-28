from AbstractEffect import Effect

import random
from Colors import Colors


class ColorFillFadeEffect(Effect):
    def __init__(self, indexes, fade_time_percent, timed_color):
        Effect.__init__(self, indexes)
        self.timed_color = timed_color
        self.fade_time_percent = fade_time_percent

    def apply(self, time_percent, parent_array):

        from_pixel = 0
        to_pixel = int(len(self.indexes) * min(1, time_percent / self.fade_time_percent) )

        for i in range(0, len(self.indexes)):
            time_to_end_percent = 1.0 - time_percent
            color = Colors.hls_to_rgb(self.timed_color.get_hue(time_percent, i), 1.0, time_to_end_percent * time_to_end_percent) if i > from_pixel and i < to_pixel else [0,0,0]
            i_in_obj = self.indexes[i]
            parent_array[i_in_obj * 3: i_in_obj * 3 + 3] = color