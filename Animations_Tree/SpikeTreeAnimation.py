from AbstractTreeAnimation import TreeAnimation

from Effects.SpikeEffect import SpikeEffect

from Colors.TimedColor import TimedColorFactory, CircularLocHue

import random

class SpikeTreeAnimation(TreeAnimation):

    def __init__(self, tree, props):
        TreeAnimation.__init__(self, tree, props)
        self.effects = []
        self.last_time = 0
        self.part = 0

        self.dir = 'clockwise'
        self.circular = False
        self.timed_color = CircularLocHue()

        if self.props is not None:
            if 'circular' in self.props:
                self.circular = self.props['circular']
            if 'color' in self.props:
                timed_color = TimedColorFactory(self.props['color'])
                if timed_color is not None:
                    self.timed_color = timed_color
            if 'dir' in self.props:
                self.dir = self.props['dir']


        self.create_effects()

    def apply(self, time_percent):
        if time_percent < self.last_time:
            self.create_effects()
        self.last_time = time_percent
        for effect in self.effects:
            effect.apply(time_percent, self.tree.get_array())

    def create_effects(self):
        self.effects = []
        self.tree.clear()
        self.beat_rand = random.random()

        for leaf in self.tree.get_left_leaf_array():
            self.effects.append(SpikeEffect(self.arr_use_dir(leaf[0], False, True), self.timed_color, 1.0, len(leaf[0]), self.circular))
            self.effects.append(SpikeEffect(self.arr_use_dir(leaf[1], True, True), self.timed_color, 1.0, len(leaf[1]), self.circular))

        for leaf in self.tree.get_right_leaf_array():
            self.effects.append(SpikeEffect(self.arr_use_dir(leaf[0], True, True), self.timed_color, 1.0, len(leaf[0]), self.circular))
            self.effects.append(SpikeEffect(self.arr_use_dir(leaf[1], False, True), self.timed_color, 1.0, len(leaf[1]), self.circular))

        self.effects.append(SpikeEffect(self.arr_use_dir(self.tree.get_top_leaf()[0], True, True), self.timed_color, 1.0, len(self.tree.get_top_leaf()[0]), self.circular))
        self.effects.append(SpikeEffect(self.arr_use_dir(self.tree.get_top_leaf()[1], False, True), self.timed_color, 1.0, len(self.tree.get_top_leaf()[1]), self.circular))

        self.effects.append(SpikeEffect(self.arr_use_dir(self.tree.get_left_stem(), True, True), self.timed_color, 1.0, len(self.tree.get_left_stem()), self.circular))
        self.effects.append(SpikeEffect(self.arr_use_dir(self.tree.get_right_stem(), False, True), self.timed_color, 1.0, len(self.tree.get_right_stem()), self.circular))

    def arr_use_dir(self, arr, dir_clockwise, dir_inside):
        if self.dir == 'clockwise':
            return arr if dir_clockwise else arr[::-1]
        if self.dir == 'counter_clockwise':
            return arr[::-1] if dir_clockwise else arr
        if self.dir == "inside":
            return arr if dir_inside else arr[::-1]
        if self.dir == "outside":
            return arr[::-1] if dir_inside else arr


