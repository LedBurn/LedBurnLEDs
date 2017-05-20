
import datetime

import Network.LedBurnProtocol as network

from UIElements.Flower import Flower
from UIElements.SmallSheep import SmallSheep
from UIElements.Grass import Grass
from UIElements.Sign import Sign
from UIElements.Lake import Lake
from UIElements.TempStick import TempStick
from UIElements.SachiMeter import SachiMeter

from Animations.GlowAnimation import GlowAnimation

class TransitionsDriver:

    def __init__(self):
        self.start_time = datetime.datetime.now()

        self.flower = Flower()
        self.sheep = SmallSheep()
        self.grass = Grass()
        self.sign = Sign()
        self.lake = Lake()
        self.temp_stick = TempStick()
        self.sachi_meter = SachiMeter()

        self.flower_animation = GlowAnimation(self.flower)
        self.grass_animation = GlowAnimation(self.grass)
        self.lake_animation = GlowAnimation(self.lake)
        self.sheep_animation = GlowAnimation(self.sheep)
        self.sign_animation = GlowAnimation(self.sign)

    def play_animations(self, curr_temerature, sachi_meter=None):

        diff_time = (datetime.datetime.now() - self.start_time).seconds
        time_percent = (diff_time % 3.0) / 3.0

        self.flower_animation.apply(time_percent)
        self.grass_animation.apply(time_percent)
        self.lake_animation.apply(time_percent)
        self.sheep_animation.apply(time_percent)
        self.sign_animation.apply(time_percent)


        network.send(flower_data=self.flower.get_array(),
                     sheep_data=self.sheep.get_array(),
                     grass_data=self.grass.get_array(),
                     sign_data=self.sign.get_array(),
                     lake_data=self.lake.get_array(),
                     temp_stick=self.temp_stick.get_array(),
                     sachi_meter=self.sachi_meter.get_array())





