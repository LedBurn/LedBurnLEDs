from SignAnimation import SignAnimation

from Effects.RainbowEffect import RainbowEffect

class RainbowSignAnimation(SignAnimation):

    def __init__(self, sign, props):
        SignAnimation.__init__(self, sign, props)
        self.effects = [RainbowEffect(self.sign.whole_sign[::-1])]


    def apply(self, time_percent):
        for effect in self.effects:
            effect.apply(time_percent, self.sign.get_array())



