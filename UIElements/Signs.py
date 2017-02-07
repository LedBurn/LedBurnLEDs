class Signs:

    # 0-14 t
    # 17-29 h
    # 35-42 l
    # 48-60 m
    # 66-68 i

    # 76-91 t
    # 92-106 h
    # 109-116 l
    # 120-132 m
    # 134-137 i

    t1 = range(0, 14)
    h1 = range(17, 29)
    l1 = range(35, 42)
    m1 = range(48, 60)
    i1 = range(66, 68)

    t2 = range(76, 91)
    h2 = range(92, 106)
    l2 = range(109, 116)
    m2 = range(120, 132)
    i2 = range(134, 137)

    def __init__(self):
        self.clear()

    def get_array(self):
        return self.arr

    def get_sign_1(self):
        return self.t1 + self.h1 + self.l1 + self.m1 + self.i1

    def get_sign_2(self):
        return self.t2 + self.h2 + self.l2 + self.m2 + self.i2

    def get_letters(self):
        return [self.t1, self.h1, self.l1, self.m1, self.i1, self.t2, self.h2, self.l2, self.m2, self.i2]

    def get_all_indexes(self):
        return self.get_sign_1() + self.get_sign_2()

    def clear(self):
        self.arr = [0, 0, 0] * 150
