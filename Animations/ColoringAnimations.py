from abc import ABCMeta, abstractmethod
from Colors import Colors


############################
# Abstract
############################

class ColoringAnimation:
    """
    Coloring animations are steady animations that just set a base coloring to the LEDs.
    Used as core animations. They aren't really moving..

    Abstract class
    """
    __metaclass__ = ABCMeta
    
    def __init__(self, indexes):
        """
        """
        self.indexes = indexes
    
    @abstractmethod
    def apply(self, parent_array):
        """
        """
        pass


class ColoringAnimation_Core(ColoringAnimation):
    def __init__(self, indexes, max_brightness):
        """
        
        """
        ColoringAnimation.__init__(self, indexes)
        self.max_brightness = max_brightness


############################
# Core
############################

class ColoringAnimation_Core_Rainbow(ColoringAnimation_Core):
    
    def __init__(self, indexes, max_brightness, num_of_rainbows):
        """
        num_of_rainbows - number of rainbows in the painting
        """
        ColoringAnimation_Core.__init__(self, indexes, max_brightness)

        self.num_of_rainbows = num_of_rainbows

    def apply(self, parent_array):

        for i in range(len(self.indexes)):
            # color
            hue = (i / float(len(self.indexes)) * self.num_of_rainbows) % 1
            color = Colors.hls_to_rgb(hue, self.max_brightness, 1.0)
        
            index = self.indexes[i]
            parent_array[index * 3:index * 3 + 3] = color

        