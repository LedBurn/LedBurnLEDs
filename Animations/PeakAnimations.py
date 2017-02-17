from abc import ABCMeta, abstractmethod
from Colors import Colors


############################
# Abstract
############################

class PeakAnimation:
    """
    The peak animations are animations that gets the time_since_last_peak.
    They can be used for slowing down after a peak.
    They all get 'speed' that indicates how fast will they slow down / or any other change.

    Abstract class
    """
    __metaclass__ = ABCMeta
    
    def __init__(self, indexes):
        """
        """
        self.indexes = indexes
    
    @abstractmethod
    def apply(self, is_change, parent_array):
        """
        is_change - boolean, yes if should change, false if not
        """
        pass


class PeakAnimation_Core(PeakAnimation):
    def __init__(self, indexes, max_brightness):
        """
        
        """
        PeakAnimation.__init__(self, indexes)
        self.max_brightness = max_brightness


############################
# Core
############################

class PeakAnimation_Core_IncreaseHue(PeakAnimation_Core):
    def __init__(self, indexes, max_brightness, startHue, diff):
        """
        startHue - [0, 1]
        diff - [0, 1] diff in hue between each change
        """
        PeakAnimation_Core.__init__(self, indexes, max_brightness)

        self.current_hue = startHue
        self.diff = diff

    def apply(self, is_change, parent_array):
        
        # change hue
        if (is_change):
            self.current_hue = (self.current_hue + self.diff) % 1

        # color
        color = Colors.hls_to_rgb(self.current_hue, self.max_brightness, 1.0)

        # apply
        for i in self.indexes:
            parent_array[i * 3:i * 3 + 3] = color


############################
# Add On
############################

        