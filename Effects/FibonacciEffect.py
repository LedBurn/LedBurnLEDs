from AbstractEffect import Effect
from Colors import Colors
import colorsys
import math

class FibonacciEffect(Effect):
    def __init__(self, indexes, strting_hue):
        Effect.__init__(self, indexes)
        self.hue = strting_hue
        self.fibonacci(1)
        self.start_fib = 1
        
    
    def apply(self, time_percent, parent_array):

        time_percent = math.pow(time_percent, 0.2)
        fib = len(self.indexes) - int(time_percent * (len(self.indexes)))+1
        fib = max(fib, int(len(self.indexes)/100.0))
        if (fib != self.start_fib):
            self.start_fib = fib
            self.start_fib = self.fibonacci(self.start_fib) 
        
        for i in range(len(self.indexes)):
            color = [0,0,0]
            if (self.hue_num_array[i] != -1):
                hue = Colors.reduce_by_1(self.hue + self.hue_num_array[i] * 0.23)
                color = [int(c*255) for c in colorsys.hsv_to_rgb(hue, 1.0, 0.25)]
            parent_array[self.indexes[i]*3 : self.indexes[i]*3+3] = color

    def fibonacci(self, start_fib):
        self.hue_num_array = [-1] * len(self.indexes)
        fib0 = start_fib
        fib1 = start_fib
        color_num = 0
        curr_led = 0
        
        while curr_led<len(self.indexes):
            for i in range(fib1):
                led_num = curr_led + i
                
                if (led_num < len(self.indexes)):
                    self.hue_num_array[led_num] = color_num

            curr_led += fib1 + 10
            color_num += 1
            
            temp = fib1
            fib1 = fib1 + fib0
            fib0 = temp

        self.num_of_colors = color_num - 1
