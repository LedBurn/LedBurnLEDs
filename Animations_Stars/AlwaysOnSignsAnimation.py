from UIElements.Signs import Signs
from Effects.AlwaysOnEffect import AlwaysOnEffect

class AlwaysOnSignsAnimation():

    def __init__(self, signs, color):
        self.signs = signs
        self.effects = [AlwaysOnEffect(self.signs.get_all_indexes(), color)]


    def apply(self, time_percent):
        for effect in self.effects:
            effect.apply(time_percent, self.signs.get_array())
