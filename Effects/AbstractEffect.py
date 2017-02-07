from abc import ABCMeta, abstractmethod

class Effect:
    __metaclass__ = ABCMeta
    
    def __init__(self, indexes):
        self.indexes = indexes
    
    @abstractmethod
    def apply(self, time_percent, parent_array): pass

