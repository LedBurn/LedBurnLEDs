from AbstractSheepAnimation import SheepAnimation
from Effects.ConfettiEffect import ConfettiEffect

class SheepConfettiAnimation(SheepAnimation):
    def __init__(self, sheep, props):
        SheepAnimation.__init__(self, sheep)

        leds_percent_per_cycle = props['leds_percent_per_cycle'] if props and 'leds_percent_per_cycle' in props else 10
        self.effect = ConfettiEffect(self.sheep.get_all_indexes(), leds_percent_per_cycle)
    
    def apply(self, time_percent):
        self.effect.apply(time_percent, self.sheep.get_array())
