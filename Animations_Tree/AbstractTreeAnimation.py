from abc import ABCMeta, abstractmethod

class TreeAnimation:
    __metaclass__ = ABCMeta

    def __init__(self, tree, props):
        self.tree = tree
        self.props = props

    @abstractmethod
    def apply(self, time_percent): pass

