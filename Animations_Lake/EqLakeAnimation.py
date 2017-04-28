from LakeAnimation import LakeAnimation

from Effects.EqEffect import EqEffect


class EqLakeAnimation(LakeAnimation):
    def __init__(self, lake, props):
        LakeAnimation.__init__(self, lake, props)
        self.effects = []

        leds_percent_per_beat = 0.4
        only_waves = True
        brightness = 1.0
        if self.props != None:
            if 'leds_percent_per_beat' in self.props:
                leds_percent_per_beat = self.props['leds_percent_per_beat']
            if 'only_waves' in self.props:
                only_waves = self.props['only_waves']
            if 'brightness' in self.props:
                brightness = self.props['brightness']

        for w in self.lake.waves_arr:
            self.effects.append(EqEffect(w, leds_percent_per_beat, brightness))

    def apply(self, time_percent):
        for effect in self.effects:
            effect.apply(time_percent, self.lake.get_array())
