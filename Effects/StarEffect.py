from AbstractEffect import Effect

from Colors import Colors

import random

class StarEffect(Effect):
    def __init__(self, indexes, timed_color, start_time, on_time_start, on_time_end, dark_time):
        """
        
        :param indexes: 
        :param timed_color: 
        :param start_time: when the star starts to shine 
        :param on_time_start: when the star receive full brightness
        :param on_time_end: when the star starts to disappear
        :param dark_time: when the star goes dark
        please use like this 0 <= start_time <= on_time_start <= on_time_end <= dark_time <= 1.0
        """
        Effect.__init__(self, indexes)
        self.timed_color = timed_color

        self.start_time = start_time
        self.on_time_start = on_time_start
        self.on_time_end = on_time_end
        self.dark_time = dark_time

    def apply(self, time_precent, parent_array):

        if time_precent > self.dark_time:
            l = 0
        elif time_precent > self.on_time_end:
            l = (self.dark_time - time_precent) / (self.dark_time - self.on_time_end)
        elif time_precent > self.on_time_start:
            l = random.uniform(0.8, 1.0)
        elif time_precent > self.start_time:
            l = (time_precent - self.start_time) / (self.on_time_start - self.start_time)
        else:
            l = 0

        color = self.timed_color.get_color(time_precent, None)
        fixed_color = Colors.change_rgb_lightness(color, Colors.fix_lightness_percent(l))

        for i in self.indexes:
            parent_array[i*3 : i*3+3] = fixed_color


