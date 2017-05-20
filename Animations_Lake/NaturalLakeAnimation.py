from LakeAnimation import LakeAnimation

from Effects.DarkPointEffect import DarkPointEffect
from Effects.AlwaysOnEffect import AlwaysOnEffect

from Colors import Colors
import random, math

class NaturalLakeAnimation(LakeAnimation):
    def __init__(self, lake, props):
        LakeAnimation.__init__(self, lake, props)
        self.effects = []
        self.previous_time = 1

        self.hue = 0.67
        if self.props != None:
            if 'hue_start' in self.props:
                self.hue = self.props['hue_start']       
        

        self.base_effect = AlwaysOnEffect(self.lake.whole_lake, Colors.hls_to_rgb(self.hue, 1, 1))

        self.start_times = []
        self.speeds = []
        self.create_effects()

    def create_effects(self): 
        self.effects = []
        self.start_times = []
        self.speeds = []

        for i in range(len(self.lake.waves_arr)):
            start_time = random.uniform(0, 0.2)
            speed = 0.8
            self.start_times.append(start_time)
            self.speeds.append(speed)

            wave = self.lake.waves_arr[i][::-1]
            self.effects.append(DarkPointEffect(wave, 10))

    
    def apply(self, time_percent):
        if (time_percent < self.previous_time):
            self.create_effects()
        self.previous_time = time_percent

        self.base_effect.apply(time_percent, self.lake.get_array())
      
        for i in range(len(self.lake.waves_arr)):
            if (time_percent < self.start_times[i] or time_percent > self.start_times[i]+self.speeds[i]):
                continue
            relative_pos = (time_percent - self.start_times[i]) / self.speeds[i]
            self.effects[i].apply(relative_pos, self.lake.get_array())
