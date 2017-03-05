class Flower:

    l1 = range(0, 29)
    l2 = range(30 ,59)
    l3 = range(60 ,89)
    l4 = range(90 ,118)
    l5 = range(119 ,149)
    l6 = range(150 ,178)
    l7 = range(179 ,208)
    l8 = range(209 ,238)
    l9 = range(239 ,269)
    l10 = range(271 ,299)

    def __init__(self):
        self.clear()

    def get_array(self):
        return self.arr

    def get_leaves(self):
        return self.l1 + self.l2 + self.l3 + self.l4 + self.l5 + self.l6 + self.l7 + self.l8 + self.l9 + self.l10

    def get_leaves_array(self):
        return [self.l1, self.l2, self.l3, self.l4, self.l5, self.l6, self.l7, self.l8, self.l9, self.l10]

    def get_seeds(self):
        return range(300, 350)

    def get_all_indexes(self):
        return self.get_leaves() + self.get_seeds()

    def clear(self):
        self.arr = [0, 0, 0] * 350
