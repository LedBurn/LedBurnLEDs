from FlowerAnimation import FlowerAnimation

from Effects.ConfettiEffect import ConfettiEffect
from Effects.AlwaysOnEffect import AlwaysOnEffect

class ConfettiFlowerAnimation(FlowerAnimation):
    def __init__(self, flower, props):
        FlowerAnimation.__init__(self, flower, props)
        self.effects = []
        whole_flower = True
        leds_percent_per_beat = 0.4
        brightness = 1.0
        fade = 0.90
        if self.props != None:
            if 'only_top' in self.props:
                whole_flower = not self.props['only_top']
            if 'leds_percent_per_beat' in self.props:
                leds_percent_per_beat = self.props['leds_percent_per_beat']
            if 'brightness' in self.props:
                brightness = self.props['brightness']
            if 'fade' in self.props:
                fade = self.props['fade']

       	if whole_flower == True:
        	self.effects.append(ConfettiEffect(self.flower.bottom_parts + self.flower.top_leaves, leds_percent_per_beat, brightness, fade))
        	self.effects.append(AlwaysOnEffect(self.flower.seeds, [0, 0, 0]))
        else:
        	self.effects.append(ConfettiEffect(self.flower.top_leaves, leds_percent_per_beat, brightness, fade))
        	self.effects.append(AlwaysOnEffect(self.flower.line, [5, 50, 0]))
	        self.effects.append(AlwaysOnEffect(self.flower.leaves, [0, 50, 0]))
	        self.effects.append(AlwaysOnEffect(self.flower.seeds, [0, 0, 0]))

    
    def apply(self, time_percent):
    	for effect in self.effects:
        	effect.apply(time_percent, self.flower.get_array())
