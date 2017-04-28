from FireSignAnimation import FireSignAnimation
from HueSignAnimation import HueSignAnimation
from RainbowSignAnimation import RainbowSignAnimation

class SignAnimationFactory():
    @staticmethod
    def create_animation(config, sign):

        print 'sign -', config

        if config == None:
            print 'Invalid sign animation - None'
            return

        if 'Hue' in config:
            return HueSignAnimation(sign, config['Hue'])

        if 'Fire' in config:
        	return FireSignAnimation(sign, config['Fire'])

        if 'Rainbow' in config:
            return RainbowSignAnimation(sign, config['Rainbow'])

        print 'Invalid sign animation -', config