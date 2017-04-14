from abc import ABCMeta, abstractmethod
from UIElements.Flower import Flower

class FlowerAnimation:
    __metaclass__ = ABCMeta
    
    def __init__(self, flower):
        self.flower = flower

    @abstractmethod
    def apply(self, time_percent): pass

