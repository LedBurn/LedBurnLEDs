from GrassAnimation import GrassAnimation

from ConfettiEffect import ConfettiEffect

class ConfettiGrassAnimation(GrassAnimation):
    def __init__(self, grass, props):
        GrassAnimation.__init__(self, grass, props)
        self.effects = []

        leds_percent_per_beat = 0.4
        brightness = 1.0
        if self.props != None:
        	if 'leds_percent_per_beat' in self.props:
        		leds_percent_per_beat = self.props['leds_percent_per_beat']
        if 'brightness' in self.props:
                brightness = self.props['brightness']
        
        self.effects.append(ConfettiEffect(self.grass.get_leaves(), leds_percent_per_beat, brightness))

    
    def apply(self, time_percent):
    	for effect in self.effects:
        	effect.apply(time_percent, self.grass.get_array())
