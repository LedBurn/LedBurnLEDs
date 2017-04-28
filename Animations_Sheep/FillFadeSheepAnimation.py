from AbstractSheepAnimation import SheepAnimation
from Effects.ColorFilleFadeEffect import ColorFillFadeEffect
from Effects.FadeInOutEffect import FadeInOutEffect
from Effects.AlwaysOnEffect import AlwaysOnEffect

from Colors.TimedColor import HueChangeTimedColor

class FillFadeSheepAnimation(SheepAnimation):
    def __init__(self, sheep, props):
        SheepAnimation.__init__(self, sheep, props)

        self.hue = 'Rainbow'
        if 'hue_start' in self.props:
            self.hue = self.props['hue_start']

        self.restart_effect()
        self.previous_time = 1

    def apply(self, time_percent):

        if time_percent < self.previous_time:
            self.restart_effect()
        self.previous_time = time_percent

        self.body_effect.apply(time_percent, self.sheep.get_array())
        self.head_effect.apply(time_percent, self.sheep.get_array())
        self.legs_effect.apply(time_percent, self.sheep.get_array())
        self.eyes_effect.apply(time_percent, self.sheep.get_array())

    def restart_effect(self):
        self.eyes_effect = AlwaysOnEffect(self.sheep.get_ears_indexes(), [255, 0, 0])

        if self.hue == 'Rainbow':
            self.head_effect = FadeInOutEffect(self.sheep.get_head_indexes(), HueChangeTimedColor(0.0, 1.0))
            self.legs_effect = FadeInOutEffect(self.sheep.get_legs_indexes(), HueChangeTimedColor(0.0, 1.0))
            self.body_effect = ColorFillFadeEffect(self.sheep.get_body_indexes(), 0.5, HueChangeTimedColor(0.0, 1.0))
        else:
            start_hue = self.hue - 0.05
            end_hue = self.hue + 0.05
            self.head_effect = FadeInOutEffect(self.sheep.get_head_indexes(), HueChangeTimedColor(start_hue, end_hue))
            self.legs_effect = FadeInOutEffect(self.sheep.get_legs_indexes(), HueChangeTimedColor(start_hue, end_hue))
            self.body_effect = ColorFillFadeEffect(self.sheep.get_body_indexes(), 0.5, HueChangeTimedColor(start_hue, end_hue))
