
import datetime

from Sensors import Decisions
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
from Animations_Tree.GlowTreeAnimation import GlowTreeAnimation
from Animations_Flower.GlowFlowerAnimation import GlowFlowerAnimation
from Animations_Grass.GlowGrassAnimation import GlowGrassAnimation
from Animations_Sign.GlowSignAnimation import GlowSignAnimation

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
        self.temp_stick.set_is_on(True)
        self.sachi_meter = SachiMeter()

        self.flower_animation = GlowFlowerAnimation(self.flower)
        self.grass_animation = GlowGrassAnimation(self.grass)
        self.lake_animation = GlowAnimation(self.lake, [0, 0, 255])
        self.sheep_animation = GlowAnimation(self.sheep, [64, 64, 64])
        self.sign_animation = GlowSignAnimation(self.sign)
        self.tree_animation = GlowTreeAnimation(self.tree)

    def play_animations(self, curr_temerature, sachi_meter, input_type):

        diff_time = (datetime.datetime.now() - self.start_time).total_seconds()
        time_percent = (diff_time % 3.0) / 3.0

        self.temp_stick.set_is_input_mode(input_type == Decisions.InputType.TEMPERATURE)
        self.sachi_meter.set_is_input_mode(input_type == Decisions.InputType.SACHI)

        self.flower_animation.apply(time_percent)
        self.grass_animation.apply(time_percent)
        self.lake_animation.apply(time_percent)
        self.sheep_animation.apply(time_percent)
        self.sign_animation.apply(time_percent)
        self.tree_animation.apply(time_percent)
        self.temp_stick.set_temperature(time_percent, curr_temerature)
        self.sachi_meter.set_sachi_meter(time_percent, sachi_meter)


        network.send(flower_data=self.flower.get_array(),
                     sheep_data=self.sheep.get_array(),
                     grass_data=self.grass.get_array(),
                     sign_data=self.sign.get_array(),
                     lake_data=self.lake.get_array(),
                     temp_stick=self.temp_stick.get_array(),
                     sachi_meter=self.sachi_meter.get_array(),
                     tree_data=self.tree.get_array())





