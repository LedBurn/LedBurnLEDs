from AbstractEffect import Effect

class SpinningFadeEffect(Effect):
    def __init__(self, indexes, color):
        Effect.__init__(self, indexes)
        self.color = color
        self.currentOnLed = -1;
    
    def apply(self, time_precent, parent_array):
        
        # current led index
        self.currentOnLed = int(time_precent * len(self.indexes))
        
        for i in range(len(self.indexes)):
            
            # calculate distance from current led
            if (i < self.currentOnLed):
                distance = min(self.currentOnLed - i, i + len(self.indexes) - self.currentOnLed)
            else:
                distance = min(i - self.currentOnLed, self.currentOnLed + len(self.indexes) - i)
                
            # calcuate color power based on distance
            power = 1 - 2*distance / float(len(self.indexes))
            power = pow(power,4)
            
            # apply
            parent_array[self.indexes[i]*3 : self.indexes[i]*3+3] = [int(self.color[0] * power),
                                                                     int(self.color[1] * power),
                                                                     int(self.color[2] * power)]




