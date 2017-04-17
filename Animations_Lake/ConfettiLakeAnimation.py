from LakeAnimation import LakeAnimation

from ConfettiEffect import ConfettiEffect
from AlwaysOnEffect import AlwaysOnEffect

class ConfettiLakeAnimation(LakeAnimation):
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
        
        if only_waves == True:
            self.effects.append(ConfettiEffect(self.lake.waves, leds_percent_per_beat, brightness))
            self.effects.append(AlwaysOnEffect(self.lake.contour, [0, 0, 30]))
        else:
            self.effects.append(ConfettiEffect(self.lake.whole_lake, leds_percent_per_beat, brightness))

    
    def apply(self, time_percent):
    	for effect in self.effects:
        	effect.apply(time_percent, self.lake.get_array())
