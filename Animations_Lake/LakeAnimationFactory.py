from RoundRobinLakeAnimation import RoundRobinLakeAnimation
from ConfettiLakeAnimation import ConfettiLakeAnimation
from NaturalLakeAnimation import NaturalLakeAnimation

class LakeAnimationFactory():
    @staticmethod
    def create_animation(config, lake):

        print 'lake -', config

        if config == None:
            print 'Invalid lake animation - None'
            return

        if 'RoundRobin' in config:
            return RoundRobinLakeAnimation(lake, config['RoundRobin'])

        if 'Confetti' in config:
        	return ConfettiLakeAnimation(lake, config['Confetti'])

        if 'Natural' in config:
            return NaturalFlowerAnimation(lake, config['Natural'])

        print 'Invalid lake animation -', config