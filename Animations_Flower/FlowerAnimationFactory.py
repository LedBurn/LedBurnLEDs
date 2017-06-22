from NaturalFlowerAnimation import NaturalFlowerAnimation
from RainbowFlowerAnimation import RainbowFlowerAnimation
from RoundRobinFlowerAnimation import RoundRobinFlowerAnimation
from ExplosionFlowerAnimation import ExplosionFlowerAnimation
from AlternateFlowerAnimation import AlternateFlowerAnimation
from FireFlowerAnimation import FireFlowerAnimation
from ConfettiFlowerAnimation import ConfettiFlowerAnimation
from SpikesFlowerAnimation import SpikesFlowerAnimation
from GlowFlowerAnimation import GlowFlowerAnimation


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

        if 'Confetti' in config:
            return ConfettiFlowerAnimation(flower, config['Confetti'])

        if 'Spikes' in config:
            return SpikesFlowerAnimation(flower, config['Spikes'])

        if 'Glow' in config:
            return GlowFlowerAnimation(flower, config['Glow'])

        print 'Invalid flower animation -', config

