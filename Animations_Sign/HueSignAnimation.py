from SignAnimation import SignAnimation
import random
from Effects.GoToColorEffect import GoToColorEffect
from Effects.AlwaysOnEffect import AlwaysOnEffect
from Colors import Colors

class HueSignAnimation(SignAnimation):
    """
    Slowly running on the hue circle
    hue_speed: [0-1] change in hue for one beat
    hue_start: [0-1] the starting hue of the first beat
    animated: True/False
    full_color: True/False - if not full color than it more white color (roundrobin of flower vs lake)
    """

    def __init__(self, sign, props):
        SignAnimation.__init__(self, sign, props)
        self.previous_time = 1

        self.animated = False
        self.full_color = True
        self.hue_speed = 0.3125
        self.hue = random.random()
        if self.props != None:
            if 'hue_speed' in self.props:
                self.hue_speed = self.props['hue_speed']
            if 'hue_start' in self.props:
                self.hue = self.props['hue_start']
            if 'animated' in self.props:
                self.animated = self.props['animated']
            if 'full_color' in self.props:
                self.full_color = self.props['full_color']

    def apply(self, time_percent):

        if time_percent < self.previous_time:
            self.next_hue()
        self.previous_time = time_percent

        for effect in self.effects:
            effect.apply(time_percent, self.sign.get_array())

    def next_hue(self):
        self.effects = []

        new_hue = self.hue + self.hue_speed
        if new_hue > 1 : new_hue -= 1
        
        if self.full_color == True:
            prev_color = Colors.hls_to_rgb(self.hue, 1.0, 1.0)
            new_color = Colors.hls_to_rgb(new_hue, 1.0, 1.0)
        else:
            prev_color = Colors.hls_to_rgb(self.hue, 0.5, 0.7)
            new_color = Colors.hls_to_rgb(new_hue, 0.5, 0.7)            

        if self.animated == True:
            self.effects.append(GoToColorEffect(self.sign.whole_sign, prev_color, new_color))
        else:
            self.effects.append(AlwaysOnEffect(self.sign.whole_sign, new_color))
        
        self.hue = new_hue



