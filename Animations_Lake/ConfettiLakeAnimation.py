from LakeAnimation import LakeAnimation

from Effects.ConfettiEffect import ConfettiEffect
from Effects.AlwaysOnEffect import AlwaysOnEffect

class ConfettiLakeAnimation(LakeAnimation):
    def __init__(self, lake, props):
        LakeAnimation.__init__(self, lake, props)
        self.effects = []

        leds_percent_per_beat = 0.4
        fade_factor = 0.9
        only_waves = True
        brightness = 1.0
        if self.props != None:
            if 'leds_percent_per_beat' in self.props:
                leds_percent_per_beat = self.props['leds_percent_per_beat']
            if 'only_waves' in self.props:
                only_waves = self.props['only_waves']
            if 'brightness' in self.props:
                brightness = self.props['brightness']
            if 'fade_factor' in self.props:
                fade_factor = self.props['fade_factor']
        
        if only_waves == True:
            self.effects.append(ConfettiEffect(self.lake.waves, leds_percent_per_beat, brightness, fade_factor=fade_factor))
            self.effects.append(AlwaysOnEffect(self.lake.contour, [0, 0, 30]))
        else:
            self.effects.append(ConfettiEffect(self.lake.whole_lake, leds_percent_per_beat, brightness, fade_factor=fade_factor))

    
    def apply(self, time_percent):
    	for effect in self.effects:
        	effect.apply(time_percent, self.lake.get_array())
