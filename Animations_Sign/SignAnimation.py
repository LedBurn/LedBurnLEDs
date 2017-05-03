from abc import ABCMeta, abstractmethod

import sys, os
sys.path.append(os.path.abspath('../UIElements'))


class SignAnimation:
    __metaclass__ = ABCMeta
    
    def __init__(self, sign, props):
        self.sign = sign
        self.props = props

    @abstractmethod
    def apply(self, time_percent): pass

