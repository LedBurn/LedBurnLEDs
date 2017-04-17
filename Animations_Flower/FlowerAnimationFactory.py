from NaturalFlowerAnimation import NaturalFlowerAnimation
from RainbowFlowerAnimation import RainbowFlowerAnimation
from RoundRobinFlowerAnimation import RoundRobinFlowerAnimation


class FlowerAnimationFactory():
    
    @staticmethod
    def create_animation(config, flower):

    	print config

    	if config == None:
    		print 'Invalid flower animation - None'
    		return

    	
    	if 'Natural' in config:
    		return NaturalFlowerAnimation(flower, config['Natural'])

    	if 'Rainbow' in  config:
    		return RainbowFlowerAnimation(flower, config['Rainbow'])

    	if 'RoundRobin' in config:
    		return RoundRobinFlowerAnimation(flower, config['RoundRobin'])

        print 'Invalid flower animation -', config
