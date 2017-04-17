from RoundRobinLakeAnimation import RoundRobinLakeAnimation
from ConfettiLakeAnimation import ConfettiLakeAnimation

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

        print 'Invalid lake animation -', config