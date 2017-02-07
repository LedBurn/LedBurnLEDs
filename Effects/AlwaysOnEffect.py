from AbstractEffect import Effect

class AlwaysOnEffect(Effect):
    def __init__(self, indexes, color):
        Effect.__init__(self, indexes)
        self.color = color
    
    def apply(self, time_precent, parent_array):
        for i in self.indexes:
            parent_array[i*3 : i*3+3] = self.color


