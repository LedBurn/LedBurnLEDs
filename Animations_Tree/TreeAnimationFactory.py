from AlternateTreeAnimation import AlternateTreeAnimation
from ConfettiTreeAnimation import ConfettiTreeAnimation
from ExplotionTreeAnimation import ExplosionTreeAnimation
from FireTreeAnimation import FireTreeAnimation
from NaturalTreeAnimation import NaturalTreeAnimation
from RainbowTreeAnimation import RainbowTreeAnimation
from RoundRobinTreeAnimation import RoundRobinTreeAnimation
from SpikeTreeAnimation import SpikeTreeAnimation
from SinglePixelTreeAnimation import SinglePixelTreeAnimation

class TreeAnimationFactory():
    @staticmethod
    def create_animation(config, tree):

        print 'tree -', config

        if config == None:
            print 'Invalid tree animation - None'
            return

        name_to_obj = {
            'Alternate' : AlternateTreeAnimation,
            'Confetti': ConfettiTreeAnimation,
            'Explosion': ExplosionTreeAnimation,
            'Fire' : FireTreeAnimation,
            'Natural' : NaturalTreeAnimation,
            'Rainbow' : RainbowTreeAnimation,
            'RoundRobin': RoundRobinTreeAnimation,
            'Spikes': SpikeTreeAnimation,
            'Pixel': SinglePixelTreeAnimation
        }

        for n, o in name_to_obj.iteritems():
            if n in config:
                return o(tree, config[n])

        print 'Invalid tree animation -', config

