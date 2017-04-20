from abc import ABCMeta, abstractmethod

class GrassAnimation:
    __metaclass__ = ABCMeta
    
    def __init__(self, grass, props):
        self.grass = grass
        self.props = props

    @abstractmethod
    def apply(self, time_percent): pass

