
import random
import math

from Colors import Colors

class GlowSignAnimation:

    def __init__(self, sign):
        self.sign = sign
        self.hues = [random.random() for _ in range(0, len(sign.get_letters()))]

    def apply(self, time_percent):

        if time_percent < 0.5:
            c = time_percent * 0.25
        else:
            c = (1.0 - time_percent) * 0.25
        c = c +0.01
        c = math.pow(c, 0.5)

        for letter_index in range(0, len(self.sign.get_letters())):
            letter = self.sign.get_letters()[letter_index]
            hue = self.hues[letter_index]
            for i in letter:
                self.sign.get_array()[i*3:i*3+3] = Colors.hls_to_rgb(hue, 1.0, c)

