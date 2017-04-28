from AbstractSheepAnimation import SheepAnimation
from Effects.SpikeEffect import SpikeEffect
from Effects.AlwaysOnEffect import AlwaysOnEffect

from Colors.TimedColor import HueChangeTimedColor
from Colors.TimedColor import HueChangeTimedColorByLocation

import random

class ColorType:
    COLOR = 0
    RAINBOW = 1

class SpikeSheepAnimation(SheepAnimation):
    def __init__(self, sheep, props):
        SheepAnimation.__init__(self, sheep, props)
        self.color_type = ColorType.RAINBOW
        if self.props != None:
            
            if 'hue_start' in self.props:
                if self.props['hue_start'] == 'Rainbow':
                    self.color_type = ColorType.RAINBOW
                else:    
                    self.color_type = ColorType.COLOR
                    self.hue = self.props['hue_start']


        self.restart_effect()
        self.previous_time = 1

    def apply(self, time_percent):

        if time_percent < self.previous_time:
            self.restart_effect()
        self.previous_time = time_percent

        for e in self.effects:
            e.apply(time_percent, self.sheep.get_array())

    def restart_effect(self):
        self.effects = []
        self.add_part(self.sheep.get_leg12_side1_indexes())
        self.add_part(self.sheep.get_leg12_side2_indexes())
        self.add_part(self.sheep.get_leg34_side1_indexes())
        self.add_part(self.sheep.get_leg34_side2_indexes())
        self.add_part(self.sheep.get_head_up1())
        self.add_part(self.sheep.get_head_up2())
        for i in range(self.sheep.get_num_of_body_parts()):
            self.add_part(self.sheep.get_body_part_indexes(i))

    def add_part(self, part):
        self.add_spike_effect(part[:len(part)/2])
        self.add_spike_effect(part[len(part)/2:][::-1])

    def add_spike_effect(self, indexes):
        first_i = random.randint(0, len(indexes)/2 - 1)
        first_i = 0
        if random.random() < 0.5:
            indexes = indexes[::-1]

        if self.color_type == ColorType.RAINBOW:
            self.effects.append(SpikeEffect(indexes, HueChangeTimedColorByLocation(0.0, 1.0), 1.0, len(indexes) * 2))
        else:
            start_hue = self.hue - 0.1
            end_hue = self.hue + 0.1
            self.effects.append(SpikeEffect(indexes, HueChangeTimedColorByLocation(start_hue, end_hue), 1.0, len(indexes) * 2))


