from LakeAnimation import LakeAnimation

from Effects.SpikeEffect import SpikeEffect
from Effects.GradientEffect import GradientEffect
from Effects.AlwaysOnEffect import AlwaysOnEffect

from Colors.TimedColor import CircularLocHue, TimedColorFactory

from Colors import Colors


class SpiningColorLakeAnimation(LakeAnimation):
    def __init__(self, lake, props):
        LakeAnimation.__init__(self, lake, props)
        self.effects = []

        self.timed_color = CircularLocHue()

        self.brightness = 0.2
        self.hue1 = 0.7
        self.hue2 = 0.8

        if self.props != None:
            if 'contour_color' in self.props:
                timed_color = TimedColorFactory(self.props['contour_color'])
                if timed_color is not None:
                    self.timed_color = timed_color

        self.effects.append(SpikeEffect(self.lake.contour, self.timed_color, 0.65, len(self.lake.contour), circular=True))

    def apply(self, time_percent):
        for effect in self.effects:
            effect.apply(time_percent, self.lake.get_array())

        for i in range(0, len(self.lake.waves_arr)):
            w = self.lake.waves_arr[i]
            conn1_i = self.lake.conn_arr[i][0]
            conn2_i = self.lake.conn_arr[i][1]
            conn1_c = self.lake.get_array()[conn1_i * 3: conn1_i * 3 + 3]
            conn2_c = self.lake.get_array()[conn2_i * 3: conn2_i * 3 + 3]
            #power values set by expirement to nice looking values
            GradientEffect(w[0:len(w) / 2], conn1_c, [0,0,0], power=0.03).apply(None, self.lake.get_array())
            GradientEffect(w[len(w) / 2:], [0,0,0], conn2_c, power=3.0).apply(None, self.lake.get_array())
