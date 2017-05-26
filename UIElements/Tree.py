class Tree:

    left_side = range(0,499)
    right_side = range(499, 1082)

    left_leafs = [[range(154, 218)[::-1], range(218,299)],
                  [range(299, 347)[::-1], range(347,413)],
                  [range(413, 449)[::-1], range(449, 499)]]

    right_leafs=[[range(661, 727)[::-1], range(727,812)],
                 [range(812, 857)[::-1], range(857, 921)],
                 [range(921, 956)[::-1], range(956, 997)]]

    top_leaf=[range(997, 1035)[::-1], range(1035,1082)]

    def get_all_indexes(self):
        return range(0, 1082)

    def get_left_stem(self):
        return range(0, 154)

    def get_right_stem(self):
        return range(499, 661)

    def get_stem(self):
        return self.get_left_stem() + self.get_right_stem()

    def get_leaves_array(self):
        return [self.top_leaf] + self.right_leafs[::-1] + self.left_leafs

    def get_leaves(self):
        return self.leaves

    def get_leaves_and_stem(self):
        return [self.top_leaf] + self.right_leafs[::-1] + [(self.get_right_stem(), self.get_left_stem())] + self.left_leafs

    def get_top_leaf(self):
        return self.top_leaf

    def get_left_leaf_array(self):
        return self.left_leafs

    def get_right_leaf_array(self):
        return self.right_leafs

    def get_left_leaf(self, i):
        return self.left_leafs[i]

    def get_right_leaf(self, i):
        return self.right_leafs[i]

    def __init__(self):
        self.clear()
        self.leaves = []
        for two_half_leaves in (self.right_leafs + self.left_leafs):
            for half_leaf in two_half_leaves:
                self.leaves = self.leaves + half_leaf
        for half_leaf in self.top_leaf:
            self.leaves = self.leaves + half_leaf

    def clear(self):
        self.arr = [0] * (1082 * 3)

    def get_array(self):
        return self.arr

