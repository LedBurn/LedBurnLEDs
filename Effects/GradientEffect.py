import math
from AbstractEffect import Effect

def animatePoint(fromColor, toColor, percent):
    r = animateInt(fromColor[0], toColor[0], percent)
    g = animateInt(fromColor[1], toColor[1], percent)
    b = animateInt(fromColor[2], toColor[2], percent)
    return [r, g, b]

def animateInt(fromInt, toInt, percent):
    if (fromInt > toInt):
        diff = fromInt - toInt
        return int(fromInt - diff*percent)
    else:
        diff = toInt - fromInt
        return int(fromInt + diff*percent)

class GradientEffect(Effect):
    def __init__(self, indexes, from_color, to_color, power):
        Effect.__init__(self, indexes)
        self.from_color = from_color
        self.to_color = to_color
        self.power = power
    
    def apply(self, time_percent, parent_array):
        for i in range(len(self.indexes)):
            index = self.indexes[i]
            percent = float(i) / len(self.indexes)
            percent = math.pow(percent, self.power)
            color = animatePoint(self.from_color, self.to_color, percent)
            parent_array[index*3 : index*3+3] = color


