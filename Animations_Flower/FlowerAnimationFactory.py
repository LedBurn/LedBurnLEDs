from NaturalFlowerAnimation import NaturalFlowerAnimation
from RainbowFlowerAnimation import RainbowFlowerAnimation
from RoundRobinFlowerAnimation import RoundRobinFlowerAnimation
from ExplosionFlowerAnimation import ExplosionFlowerAnimation
from AlternateFlowerAnimation import AlternateFlowerAnimation
from FireFlowerAnimation import FireFlowerAnimation


class FlowerAnimationFactory():
    
    @staticmethod
    def create_animation(config, flower):

    	print 'flower -', config

    	if config == None:
    		print 'Invalid flower animation - None'
    		return

    	
    	if 'Natural' in config:
    		return NaturalFlowerAnimation(flower, config['Natural'])

    	if 'Rainbow' in  config:
    		return RainbowFlowerAnimation(flower, config['Rainbow'])

    	if 'RoundRobin' in config:
    		return RoundRobinFlowerAnimation(flower, config['RoundRobin'])

        if 'Alternate' in config:
            return AlternateFlowerAnimation(flower, config['Alternate'])

        if 'Explosion' in config:
            return ExplosionFlowerAnimation(flower, config['Explosion'])

        if 'Fire' in config:
            return FireFlowerAnimation(flower, config['Fire'])

        print 'Invalid flower animation -', config

