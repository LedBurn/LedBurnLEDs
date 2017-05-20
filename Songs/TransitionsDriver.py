
import datetime

import Network.LedBurnProtocol as network

from UIElements.Flower import Flower
from UIElements.SmallSheep import SmallSheep
from UIElements.Grass import Grass
from UIElements.Sign import Sign
from UIElements.Lake import Lake
from UIElements.Tree import Tree
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
        self.tree = Tree()
        self.temp_stick = TempStick()
        self.sachi_meter = SachiMeter()

        self.flower_animation = GlowAnimation(self.flower, [0, 255, 0])
        self.grass_animation = GlowAnimation(self.grass, [255, 255, 0])
        self.lake_animation = GlowAnimation(self.lake, [0, 0, 255])
        self.sheep_animation = GlowAnimation(self.sheep, [255, 255, 255])
        self.sign_animation = GlowAnimation(self.sign, [255, 0, 0])
        self.tree_animation = GlowAnimation(self.tree, [0, 255, 0])

    def play_animations(self, curr_temerature, sachi_meter=None):

        diff_time = (datetime.datetime.now() - self.start_time).total_seconds()
        time_percent = (diff_time % 3.0) / 3.0

        self.flower_animation.apply(time_percent)
        self.grass_animation.apply(time_percent)
        self.lake_animation.apply(time_percent)
        self.sheep_animation.apply(time_percent)
        self.sign_animation.apply(time_percent)
        self.tree_animation.apply(time_percent)


        network.send(flower_data=self.flower.get_array(),
                     sheep_data=self.sheep.get_array(),
                     grass_data=self.grass.get_array(),
                     sign_data=self.sign.get_array(),
                     lake_data=self.lake.get_array(),
                     temp_stick=self.temp_stick.get_array(),
                     sachi_meter=self.sachi_meter.get_array(),
                     tree_data=self.tree.get_array())





