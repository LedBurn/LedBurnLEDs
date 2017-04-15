from abc import ABCMeta, abstractmethod

import sys, os
sys.path.append(os.path.abspath('../UIElements'))
from Sign import Sign

class FlowerAnimation:
    __metaclass__ = ABCMeta
    
    def __init__(self, flower):
        self.flower = flower

    @abstractmethod
    def apply(self, time_percent): pass

