from AbstractEffect import Effect

from Colors import Colors

class FadeInOutEffect(Effect):
    def __init__(self, indexes, timed_color):
        Effect.__init__(self, indexes)
        self.timed_color = timed_color

    def apply(self, time_precent, parent_array):

        if (time_precent < 0.5):
            power = 1 - time_precent * 2
        else:
            power = (time_precent - 0.5) * 2
        fixed_power = Colors.fix_lightness_percent(power)

        color = self.timed_color.get_color(time_precent, None)
        fixed_color = Colors.change_rgb_lightness(color, fixed_power)

        for i in self.indexes:
            parent_array[i*3 : i*3+3] = fixed_color


