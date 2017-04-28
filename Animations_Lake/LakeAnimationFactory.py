from RoundRobinLakeAnimation import RoundRobinLakeAnimation
from ConfettiLakeAnimation import ConfettiLakeAnimation
from NaturalLakeAnimation import NaturalLakeAnimation
from EqLakeAnimation import EqLakeAnimation

class LakeAnimationFactory():
    @staticmethod
    def create_animation(config, lake):

        print 'lake -', config

        if config == None:
            print 'Invalid lake animation r- None'
            return

        if 'RoundRobin' in config:
            return RoundRobinLakeAnimation(lake, config['RoundRobin'])

        if 'Confetti' in config:
        	return ConfettiLakeAnimation(lake, config['Confetti'])

        if 'Natural' in config:
            return NaturalLakeAnimation(lake, config['Natural'])

        if 'Eq' in config:
            return EqLakeAnimation(lake, config['Eq'])

        print 'Invalid lake animation -', config