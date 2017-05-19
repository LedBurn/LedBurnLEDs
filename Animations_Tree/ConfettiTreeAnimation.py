from AbstractTreeAnimation import TreeAnimation
from Effects.ConfettiEffect import ConfettiEffect


class ConfettiTreeAnimation(TreeAnimation):
    def __init__(self, tree, props):
        TreeAnimation.__init__(self, tree, props)

        leds_percent_per_beat = 0.4
        brightness = 1.0
        if self.props != None:
            if 'leds_percent_per_beat' in self.props:
                leds_percent_per_beat = self.props['leds_percent_per_beat']
            if 'brightness' in self.props:
                brightness = self.props['brightness']

        self.effect = ConfettiEffect(self.tree.get_all_indexes(), leds_percent_per_beat, brightness)

    def apply(self, time_percent):
        self.effect.apply(time_percent, self.tree.get_array())
