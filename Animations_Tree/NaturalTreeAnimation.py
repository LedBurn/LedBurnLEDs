from AbstractTreeAnimation import TreeAnimation
from Effects.AlwaysOnEffect import AlwaysOnEffect
from Effects.GreenFireEffect import GreenFireEffect


class NaturalTreeAnimation(TreeAnimation):
    def __init__(self, tree, props):
        TreeAnimation.__init__(self, tree, props)

        self.effects = []
        self.effects.append(AlwaysOnEffect(self.tree.get_stem(), [184, 134, 11]))
        for leaf in self.tree.get_leaves_array():
            self.effects.append(GreenFireEffect(leaf[0][::-1]))
            self.effects.append(GreenFireEffect(leaf[1][::-1]))

    def apply(self, time_percent):
        for effect in self.effects:
            effect.apply(time_percent, self.tree.get_array())
