import math
from AbstractEffect import Effect

class FadeInEffect(Effect):
    def __init__(self, indexes, color):
        Effect.__init__(self, indexes)
        self.color = color
    
    def apply(self, time_percent, parent_array):
        time_percent = math.pow(time_percent, 3)
        for i in self.indexes:
            parent_array[i*3 : i*3+3] = [
                int(self.color[0] * time_percent),
                int(self.color[1] * time_percent),
                int(self.color[2] * time_percent)]


