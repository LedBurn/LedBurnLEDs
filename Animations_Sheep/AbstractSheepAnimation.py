from abc import ABCMeta, abstractmethod
from UIElements.AbstractSheep import Sheep

class SheepAnimation:
    __metaclass__ = ABCMeta
    
    def __init__(self, sheep):
        self.sheep = sheep

    @abstractmethod
    def apply(self, time_percent): pass

