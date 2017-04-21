from abc import ABCMeta, abstractmethod

import sys, os
sys.path.append(os.path.abspath('../UIElements'))

class SheepAnimation:
    __metaclass__ = ABCMeta
    
    def __init__(self, sheep):
        self.sheep = sheep

    @abstractmethod
    def apply(self, time_percent): pass

