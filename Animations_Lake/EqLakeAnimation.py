from LakeAnimation import LakeAnimation

from Effects.EqEffect import EqEffect
from Effects.GradientEffect import GradientEffect
from Effects.AlwaysOnEffect import AlwaysOnEffect

from Colors import Colors


class EqLakeAnimation(LakeAnimation):
    def __init__(self, lake, props):
        LakeAnimation.__init__(self, lake, props)
        self.effects = []

        self.brightness = 0.2
        self.hue1 = 0.7
        self.hue2 = 0.8

        if self.props != None:
            if 'hue1' in self.props:
                self.hue1 = self.props['hue1']
            if 'hue2' in self.props:
                self.hue2 = self.props['hue2']
            if 'brightness' in self.props:
                self.brightness = self.props['brightness']

        for i in range(0, len(self.lake.waves_arr)):
            w = self.lake.waves_arr[i]
            self.effects.append(EqEffect(w, brightness = self.brightness, hue1=self.hue1, hue2=self.hue2))

        #the lake segments between the waves
        for i in range(1, len(self.lake.waves_arr)):
            high_indexes = range(self.lake.conn_arr[i][0], self.lake.conn_arr[i-1][0])
            low_indexes = range(self.lake.conn_arr[i-1][1], self.lake.conn_arr[i][1])
            self.effects.append(AlwaysOnEffect(high_indexes, Colors.hls_to_rgb(self.hue1, 1.0, self.brightness)))
            self.effects.append(AlwaysOnEffect(low_indexes, Colors.hls_to_rgb(self.hue2, 1.0, self.brightness)))

        #make nice transitions in the corners
        self.effects.append(GradientEffect(range(self.lake.conn_arr[0][0], self.lake.conn_arr[0][1]), Colors.hls_to_rgb(self.hue1, 1.0, self.brightness), Colors.hls_to_rgb(self.hue2, 1.0, self.brightness)))
        self.effects.append(GradientEffect(range(self.lake.conn_arr[12][1], self.lake.conn_arr[12][0]), Colors.hls_to_rgb(self.hue2, 1.0, self.brightness), Colors.hls_to_rgb(self.hue1, 1.0, self.brightness)))

    def apply(self, time_percent):
        for effect in self.effects:
            effect.apply(time_percent, self.lake.get_array())
