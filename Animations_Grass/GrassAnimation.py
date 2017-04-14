from abc import ABCMeta, abstractmethod

import sys, os
sys.path.append(os.path.abspath('../UIElements'))
from Grass import Grass


start_color = [0, 255, 0]
end_color = [0, 50 , 50]

class GrassAnimation:
    __metaclass__ = ABCMeta
    
    def __init__(self, grass):
        self.grass = grass

    @abstractmethod
    def apply(self, time_percent): pass

