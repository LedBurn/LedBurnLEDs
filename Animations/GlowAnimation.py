
import random

from Colors import Colors

class GlowAnimation:

    def __init__(self, ui_element):
        self.ui_element = ui_element
        self.rand_hue = random.random()

    def apply(self, time_percent):

        if time_percent < 0.5:
            c = time_percent * 0.3
        else:
            c = (1.0 - time_percent) * 0.3
        c = c + 0.07

        for i in self.ui_element.get_all_indexes():
            self.ui_element.get_array()[i*3:i*3+3] = Colors.hls_to_rgb(self.rand_hue, 1.0, c)

