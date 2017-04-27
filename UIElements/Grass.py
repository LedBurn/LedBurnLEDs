class Grass:

    l1_up   = range(0, 20)
    l1_down = range(20, 39)

    l2_up   = range(42, 82)
    l2_down = range(82, 122)

    l3_up   = range(129, 166)
    l3_down = range(166, 204)

    l4_up   = range(209, 246)
    l4_down = range(246, 282)

    l5_up   = range(287, 293)
    l5_down = range(293, 298)

    l6_up   = range(301, 322)
    l6_down = range(322, 345)

    l7_up   = range(350, 366)
    l7_down = range(366, 381)

    l8_up   = range(388, 411)
    l8_down = range(411, 434)

    l9_up   = range(556, 578)
    l9_down = range(578, 600)

    l10_up   = range(436, 481)
    l10_down = range(481, 523)

    l11_up   = range(531, 541)
    l11_down = range(541, 551)

    def __init__(self):
        self.clear()

    def clear(self):
        self.arr = [0, 0, 0] * (600 + 800)

    def get_array(self):
        return self.arr

    def get_leaves(self):
        return self.l1_up + self.l1_down + \
            self.l2_up + self.l2_down + \
            self.l3_up + self.l3_down + \
            self.l4_up + self.l4_down + \
            self.l5_up + self.l5_down + \
            self.l6_up + self.l6_down + \
            self.l7_up + self.l7_down + \
            self.l8_up + self.l8_down + \
            self.l9_up + self.l9_down + \
            self.l10_up + self.l10_down + \
            self.l11_up + self.l11_down

    def get_leaves_array(self):
        return [[self.l1_up, self.l1_down], 
                [self.l2_up, self.l2_down], 
                [self.l3_up, self.l3_down],
                [self.l4_up, self.l4_down], 
                [self.l5_up, self.l5_down], 
                [self.l6_up, self.l6_down], 
                [self.l7_up, self.l7_down], 
                [self.l8_up, self.l8_down], 
                [self.l9_up, self.l9_down], 
                [self.l10_up, self.l10_down], 
                [self.l11_up, self.l11_down]]

