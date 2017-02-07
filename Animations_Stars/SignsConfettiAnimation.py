from UIElements.Signs import Signs
from Effects.ConfettiEffect import ConfettiEffect

class SignsConfettiAnimation():

    def __init__(self, signs, leds_percent_per_cycle):
        self.signs = signs
        self.effect = ConfettiEffect(self.signs.get_all_indexes(), leds_percent_per_cycle * 2)


    def apply(self, time_percent):
        self.effect.apply(time_percent, self.signs.get_array())
