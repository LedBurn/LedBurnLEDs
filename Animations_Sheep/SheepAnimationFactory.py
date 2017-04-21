from SheepConfettiAnimation import SheepConfettiAnimation
from RainbowAnimation import RainbowAnimation
from FillFadeSheepAnimation import FillFadeSheepAnimation
from StarsSheepAnimation import StarsSheepAnimation
from SpikeSheepAnimation import SpikeSheepAnimation

class SheepAnimationFactory():
    @staticmethod
    def create_animation(config, sheep):

        print 'sheep -', config

        if config == None:
            print 'Invalid sheep animation - None'
            return

        name_to_obj = {
            'Confetti': SheepConfettiAnimation,
            'Rainbow': RainbowAnimation,
            'FillFade': FillFadeSheepAnimation,
            'Stars': StarsSheepAnimation,
            'Spikes': SpikeSheepAnimation
        }

        for n, o in name_to_obj.iteritems():
            if n in config:
                return o(sheep, config[n])

        print 'Invalid sheep animation -', config

