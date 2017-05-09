
import math

from GrassAnimation import GrassAnimation
from Colors.TimedColor import HueChangeTimedColor, TimedColorFactory
from Colors import Colors
from Effects.AlwaysOnEffect import AlwaysOnEffect

class SwipeGrassAnimation(GrassAnimation):

    def __init__(self, grass, props):
        GrassAnimation.__init__(self, grass, props)

        self.timed_color = HueChangeTimedColor(0.0, 1.0)

        if self.props != None:
            if 'color' in self.props:
                timed_color = TimedColorFactory(self.props['color'])
                if timed_color is not None:
                    self.timed_color = timed_color

    def apply(self, time_percent):
        for i in range(0, self.grass.num_of_leaves()):
            leaf = self.grass.get_leaves_array()[i]
            loc = self.grass.leaf_loc_percent(i)
            c = self.timed_color.get_color(time_percent, loc)
            brightness = self.loc_to_brightness(time_percent, loc) * self.global_brightness(time_percent)
            c = Colors.change_rgb_lightness(c, Colors.fix_lightness_percent(brightness))
            AlwaysOnEffect(leaf[0] + leaf[1], c).apply(time_percent, self.grass.get_array())

    def global_brightness(self, time_percent):
        # time_percent goes from 0 to 0.5 to 0
        d = abs(0.5 - time_percent)
        return 1.0 - 2 * d

    def loc_to_brightness(self, time_percent, loc_percent):
        dist = abs(time_percent - loc_percent)
        dist = dist * 7
        return math.exp(-dist*dist)


