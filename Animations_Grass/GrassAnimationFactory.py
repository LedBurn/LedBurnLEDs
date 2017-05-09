from FireGrassAnimation import FireGrassAnimation
from HorLineGrassAnimation import HorLineGrassAnimation
from RoundRobinGrassAnimation import RoundRobinGrassAnimation
from SpikeGrassAnimation import SpikeGrassAnimation
from ConfettiGrassAnimation import ConfettiGrassAnimation
from StarsGrassAnimation import StarsGrassAnimation

class GrassAnimationFactory():
    @staticmethod
    def create_animation(config, grass):

        print 'grass -', config

        if config == None:
            print 'Invalid grass animation - None'
            return

        if 'HorLine' in config:
            return HorLineGrassAnimation(grass, config['HorLine'])

        if 'RoundRobin' in config:
            return RoundRobinGrassAnimation(grass, config['RoundRobin'])

        if 'Spike' in config:
            return SpikeGrassAnimation(grass, config['Spike'])

        if 'Fire' in config:
            return FireGrassAnimation(grass, config['Fire'])

        if 'Confetti' in config:
            return ConfettiGrassAnimation(grass, config['Confetti'])

        if 'Stars' in config:
            return StarsGrassAnimation(grass, config['Stars'])

        if 'Swipe' in config:
            return StarsGrassAnimation(grass, config['Swipe'])

        if 'Alternate' in config:
            return StarsGrassAnimation(grass, config['Alternate'])

        print 'Invalid grass animation -', config

