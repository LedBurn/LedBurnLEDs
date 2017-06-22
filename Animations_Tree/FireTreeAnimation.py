from AbstractTreeAnimation import TreeAnimation

from Effects.FireEffect import FireEffect

class FireTreeAnimation(TreeAnimation):
    def __init__(self, tree, props):
        TreeAnimation.__init__(self, tree, props)
        self.effects = []
        for leaf in self.tree.get_leaves_array():
            self.effects.append(FireEffect(leaf[0][::-1]))
            self.effects.append(FireEffect(leaf[1][::-1]))
        self.effects.append(FireEffect(self.tree.get_right_stem()))
        self.effects.append(FireEffect(self.tree.get_left_stem()))


    def apply(self, time_percent):
        for effect in self.effects:
            effect.apply(time_percent, self.tree.get_array())




