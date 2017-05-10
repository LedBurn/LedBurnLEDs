from RoundRobinLakeAnimation import RoundRobinLakeAnimation
from ConfettiLakeAnimation import ConfettiLakeAnimation
from NaturalLakeAnimation import NaturalLakeAnimation
from EqLakeAnimation import EqLakeAnimation
from SpiningColorLakeAnimation import SpiningColorLakeAnimation
from StarsLakeAnimation import StarsLakeAnimation
from FireLakeAnimation import FireLakeAnimation

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

        if 'Spin' in config:
            return SpiningColorLakeAnimation(lake, config['Spin'])

        if 'Stars' in config:
            return StarsLakeAnimation(lake, config['Stars'])

        if 'Fire' in config:
            return FireLakeAnimation(lake, config['Fire'])

        print 'Invalid lake animation -', config