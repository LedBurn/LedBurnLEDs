from AbstractSheepAnimation import SheepAnimation
from Effects.ConfettiEffect import ConfettiEffect

class SheepConfettiAnimation(SheepAnimation):
    def __init__(self, sheep, props):
        SheepAnimation.__init__(self, sheep, props)

        leds_percent_per_beat = 0.4
        brightness = 1.0
        if self.props != None:
            if 'leds_percent_per_beat' in self.props:
                leds_percent_per_beat = self.props['leds_percent_per_beat']
            if 'brightness' in self.props:
                brightness = self.props['brightness']

        self.effect = ConfettiEffect(self.sheep.get_all_indexes(), leds_percent_per_beat, brightness)
    
    def apply(self, time_percent):
        self.effect.apply(time_percent, self.sheep.get_array())
