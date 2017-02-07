import math
from AbstractEffect import Effect

class FadeOutEffect(Effect):
    def __init__(self, indexes, color):
        Effect.__init__(self, indexes)
        self.color = color
        self.to_color = [0,0,0]
        self.power = 3

    @classmethod
    def initLimit(cls, indexes, color, to_color, power):
        effect = cls(indexes, color)
        effect.to_color = to_color
        effect.power = power
        return effect
            
    
    def apply(self, time_percent, parent_array):
        power = math.pow(time_percent, self.power)
        #print str(time_percent) " - " str(power)
        
        r_diff = self.color[0] - self.to_color[0]
        r = int(self.color[0] - r_diff * power)
        
        g_diff = self.color[1] - self.to_color[1]
        g = int(self.color[1] - g_diff * power)

        b_diff = self.color[2] - self.to_color[2]
        b = int(self.color[2] - b_diff * power)

        for i in self.indexes:
            parent_array[i*3 : i*3+3] = [r, g, b]

    


