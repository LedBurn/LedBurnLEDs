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

    l12_up   = range(600, 635)
    l12_down = range(635, 668)

    l13_up   = range(671, 683)
    l13_down = range(683, 695)

    l14_up   = range(700, 729)
    l14_down = range(729, 757)

    l15_up   = range(765, 781)
    l15_down = range(781, 795)

    l16_up   = range(801, 838)
    l16_down = range(838, 875)

    l17_up   = range(878, 888)
    l17_down = range(888, 898)

    l18_up   = range(900, 920)
    l18_down = range(920, 940)

    l19_up   = range(940, 971)
    l19_down = range(972, 1002)

    l20_up   = range(1002, 1015)
    l20_down = range(1015, 1029)

    l21_up   = range(1029, 1047)
    l21_down = range(1048, 1062)

    l22_up   = range(1068, 1104)
    l22_down = range(1105, 1141)

    l23_up   = range(1146, 1157)
    l23_down = range(1157, 1169)

    l24_up   = range(1173, 1196)
    l24_down = range(1196, 1214)

    l25_up   = range(1225, 1278)
    l25_down = range(1278, 1329)

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
            self.l11_up + self.l11_down + \
            self.l12_up + self.l12_down + \
            self.l13_up + self.l13_down + \
            self.l14_up + self.l14_down + \
            self.l15_up + self.l15_down + \
            self.l16_up + self.l16_down + \
            self.l17_up + self.l17_down + \
            self.l18_up + self.l18_down + \
            self.l19_up + self.l19_down + \
            self.l20_up + self.l20_down + \
            self.l21_up + self.l21_down + \
            self.l22_up + self.l22_down + \
            self.l23_up + self.l23_down + \
            self.l24_up + self.l24_down + \
            self.l25_up + self.l25_down

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
                [self.l11_up, self.l11_down],
                [self.l12_up, self.l12_down],
                [self.l13_up, self.l13_down],
                [self.l14_up, self.l14_down],
                [self.l15_up, self.l15_down],
                [self.l16_up, self.l16_down],
                [self.l17_up, self.l17_down],
                [self.l18_up, self.l18_down],
                [self.l19_up, self.l19_down],
                [self.l20_up, self.l20_down],
                [self.l21_up, self.l21_down],
                [self.l22_up, self.l22_down],
                [self.l23_up, self.l23_down],
                [self.l24_up, self.l24_down],
                [self.l25_up, self.l25_down]]


if __name__ == "__main__":
    import Network.LedBurnProtocol

    g = Grass()
    la = g.get_leaves_array()
    for i in la[len(la) - 1][0]:
        g.get_array()[i*3:i*3+3] = [255, 0, 0]
    for i in la[len(la) - 1][1]:
        g.get_array()[i*3:i*3+3] = [0, 255, 0]
    Network.LedBurnProtocol.send(0, grass_data=g.get_array())