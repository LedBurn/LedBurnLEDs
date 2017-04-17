from abc import ABCMeta, abstractmethod

class LakeAnimation:
    __metaclass__ = ABCMeta
    
    def __init__(self, lake, props):
        self.lake = lake
        self.props = props

    @abstractmethod
    def apply(self, time_percent): pass

