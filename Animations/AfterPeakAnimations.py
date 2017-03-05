from abc import ABCMeta, abstractmethod
from Colors import Colors


############################
# Abstract
############################

class AfterPeakAnimation:
    """
    The after peak animations are animations that gets the time_since_last_peak.
    They can be used for slowing down after a peak.
    They all get 'speed' that indicates how fast will they slow down / or any other change.

    Abstract class
    """
    __metaclass__ = ABCMeta
    
    def __init__(self, indexes, speed):
        """
        speed - the time in seconds before the animation totaly stop - use float
        """
        self.indexes = indexes
        self.speed = speed
    
    @abstractmethod
    def apply(self, time_since_last_peak, parent_array):
        """
        time_since_last_peak - in seconds - use float
        """
        pass


############################
# Add On
############################

class AfterPeakAnimation_AddOn_BrightnessLoss(AfterPeakAnimation):
    def __init__(self, indexes, speed):
        """
        """
        AfterPeakAnimation.__init__(self, indexes, speed)

    def apply(self, time_since_last_peak, parent_array):
        
        # brightness level
        time_since_last_peak = min(time_since_last_peak, self.speed)
        brightness = 1 - (float(time_since_last_peak) / self.speed)

        # apply
        for i in self.indexes:
            parent_array[i * 3:i * 3 + 3] = Colors.reduce_brightness(parent_array[i * 3:i * 3 + 3], brightness)


class AfterPeakAnimation_AddOn_Circle(AfterPeakAnimation):
    def __init__(self, indexes, speed):
        """
        """
        AfterPeakAnimation.__init__(self, indexes, speed)

    def apply(self, time_since_last_peak, parent_array):

        # diff in number of leds
        time_since_last_peak = min(time_since_last_peak, self.speed)
        degree = float(time_since_last_peak) / self.speed
        diff = degree * len(self.indexes)

        # calculate new colors based on position
        new_color_array = [None] * len(self.indexes)
        for i in range(len(self.indexes)):
            print i
            print self.indexes[i]
            index = self.indexes[int((i + diff) % len(self.indexes))]
            print diff
            print index
            new_color_array[i] = parent_array[index * 3:index * 3 + 3]

        # apply
        for i in range(len(self.indexes)):
            index = self.indexes[i]
            parent_array[index * 3:index * 3 + 3] = new_color_array[i]


