from abc import ABCMeta, abstractmethod

class FlowerAnimation:
    __metaclass__ = ABCMeta
    
    def __init__(self, flower, props):
        self.flower = flower
        self.props = props

    @abstractmethod
    def apply(self, time_percent): pass