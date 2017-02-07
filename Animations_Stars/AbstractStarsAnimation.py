from abc import ABCMeta, abstractmethod
from UIElements.Stars import Stars

class AbstractStarsAnimation:
    __metaclass__ = ABCMeta
    
    def __init__(self, stars):
        self.stars = stars

    @abstractmethod
    def apply(self, time_percent): pass

