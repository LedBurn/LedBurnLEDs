from AbstractEffect import Effect

class FadeInOutEffect(Effect):
    def __init__(self, indexes, color):
        Effect.__init__(self, indexes)
        self.color = color
    
    def apply(self, time_precent, parent_array):
        for i in self.indexes:
            if (time_precent < 0.5):
                power = 1 - time_precent * 2
            else:
                power = (time_precent - 0.5) * 2
            parent_array[i*3 : i*3+3] = [int(self.color[0] * power),
                                        int(self.color[1] * power),
                                        int(self.color[2] * power)]


