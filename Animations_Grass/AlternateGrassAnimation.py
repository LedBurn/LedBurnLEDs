
import random
from GrassAnimation import GrassAnimation
from Colors import Colors
from Effects.AlternateColorEvery3Effect import AlternateColorEvery3Effect

class AlternateGrassAnimation(GrassAnimation):

    def __init__(self, grass, props):
        GrassAnimation.__init__(self, grass, props)
        self.previous_time = 1
        self.effects = []
        self.cycle_num = 0

    def create_effects(self):
        self.effects = []

        color1 = Colors.hls_to_rgb(self.hue1, 1, 1)
        color2 = Colors.hls_to_rgb(self.hue2, 1, 1)

        for l in self.grass.get_leaves_array():
            self.effects.append(AlternateColorEvery3Effect(l[0], color1, color2))
            self.effects.append(AlternateColorEvery3Effect(l[1][:], color1, color2))

    def random_hue(self):
        self.hue1 = random.random()
        self.hue2 = self.hue1 + 0.3 + random.random()*0.4
        if self.hue2 > 1 : self.hue2 - 1

    def apply(self, time_percent):
        if (time_percent < self.previous_time):

            if (self.cycle_num % 4 == 0):
                self.random_hue()
                self.create_effects()

            self.cycle_num += 1

        for effect in self.effects:
            effect.apply(time_percent, self.grass.get_array())

        self.previous_time = time_percent

