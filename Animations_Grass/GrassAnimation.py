from abc import ABCMeta, abstractmethod

import sys, os
sys.path.append(os.path.abspath('../UIElements'))
from Grass import Grass

class GrassAnimation:
    __metaclass__ = ABCMeta
    
    def __init__(self, grass):
        self.grass = grass

    @abstractmethod
    def apply(self, time_percent): pass

