from RoundRobinLakeAnimation import RoundRobinLakeAnimation

class LakeAnimationFactory():
    @staticmethod
    def create_animation(config, lake):

        print 'lake -', config

        if config == None:
            print 'Invalid lake animation - None'
            return

        if 'RoundRobin' in config:
            return RoundRobinLakeAnimation(lake, config['RoundRobin'])

        print 'Invalid lake animation -', config