from GrassAnimation import GrassAnimation

import sys, os
sys.path.append(os.path.abspath('../Effects'))
from SpikeEffect import SpikeEffect


sys.path.append(os.path.abspath('../Colors'))
from Colors import Colors

import random, colorsys

class DirectionType:
    ALL_UP = 0
    ALL_DOWN = 1
    ONE_UP_ONE_DOWN = 2

class LeafChooseType:
    ALL_LEAFS = 0
    SINGLE_RANDOM = 1
    SINGLE_SEQUENCE = 2

class LeafColorType:
    GREENISH = 0
    RAINBOW = 1


class SpikeGrassAnimation(GrassAnimation):

    def __init__(self, grass, props):

                 # direction_type = DirectionType.ALL_UP, leaf_choose_type = LeafChooseType.ALL_LEAFS, leaf_color = LeafColorType.GREENISH):
        GrassAnimation.__init__(self, grass, props)
        self.previous_time = 1
        self.last_leaf = 0 # used when self.leaf_choose_type == LeafChooseType.SINGLE_SEQUENCE

        self.direction_type = DirectionType.ALL_UP
        self.leaf_choose_type = LeafChooseType.ALL_LEAFS
        self.leaf_color = LeafColorType.GREENISH
        if self.props != None:
            if 'directionType' in self.props:
                directionType = self.props['directionType']
                if directionType == 'Up':
                    self.direction_type = DirectionType.ALL_UP
                elif directionType == 'Down':
                    self.direction_type = DirectionType.ALL_DOWN
                elif directionType == 'UpAndDown':
                    self.direction_type = DirectionType.ONE_UP_ONE_DOWN
            if 'leafChooseType' in self.props:
                leafChooseType = self.props['leafChooseType']
                if leafChooseType == 'All':
                    self.leaf_choose_type = LeafChooseType.ALL_LEAFS
                if leafChooseType == 'SingleRandom':
                    self.leaf_choose_type = LeafChooseType.SINGLE_RANDOM
                if leafChooseType == 'SingleSequence':
                    self.leaf_choose_type = LeafChooseType.SINGLE_SEQUENCE
            if 'colorType' in self.props:
                colorType = self.props['colorType']
                if colorType == 'Rainbow':
                    self.leaf_color = LeafColorType.RAINBOW
                elif colorType == 'Greenish':
                    self.leaf_color == LeafColorType.GREENISH

        self.max_height = 0
        for leaf in self.grass.get_leaves_array():
            self.max_height = max(self.max_height, len(leaf[0]))
            self.max_height = max(self.max_height, len(leaf[1]))
        self.max_height += 2 # solves a bug in a dirty way

        self.init_animations()

    def apply(self, time_percent):

        if time_percent < self.previous_time:
            self.init_animations()
        self.previous_time = time_percent

        for effect in self.effects:
            effect.apply(time_percent, self.grass.get_array())

    def init_animations(self):
        self.effects = []

        if self.leaf_choose_type == LeafChooseType.ALL_LEAFS:
            for leaf in self.grass.get_leaves_array():
                self.add_for_single_leaf(leaf)
        elif self.leaf_choose_type == LeafChooseType.SINGLE_RANDOM:
            self.add_for_single_leaf(self.grass.get_leaves_array()[random.randint(0, len(self.grass.get_leaves_array())-1)])
        elif self.leaf_choose_type == LeafChooseType.SINGLE_SEQUENCE:
            self.add_for_single_leaf(self.grass.get_leaves_array()[self.last_leaf])
            self.last_leaf += 1
            if self.last_leaf >= len(self.grass.get_leaves_array()):
                self.last_leaf = 0

    def get_rand_leaf_color(self):
        if self.leaf_color == LeafColorType.GREENISH:
            return [int(c*255) for c in colorsys.hsv_to_rgb(0.33, random.uniform(0.5, 1), random.uniform(0.5, 1))]
        elif self.leaf_color == LeafColorType.RAINBOW:
            return [int(c*255) for c in colorsys.hsv_to_rgb(random.random(), 1.0, 1.0)]

    def add_for_single_leaf(self, leaf):
        rand_leaf_color = self.get_rand_leaf_color()
        self.effects.append(
            SpikeEffect(leaf[0][:: 1 if self.direction_type == DirectionType.ALL_UP else -1], rand_leaf_color, 0.5,
                        self.max_height))
        self.effects.append(
            SpikeEffect(leaf[1][:: 1 if self.direction_type == DirectionType.ALL_DOWN else -1], rand_leaf_color, 0.5,
                        self.max_height))


