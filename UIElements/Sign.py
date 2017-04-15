class Sign:

    a = range(0, 16)
    s = range(18, 39)
    l = range(43, 55)
    i = range(60, 64)
    o = range(67, 73)
    t = range(74, 90)

    a_bottom_to_top = [10, 4, 11, 5, 12 ,6, 9, 3, 7, 3, 2, 13, 1, 14, 0, 14]
    s_bottom_to_top = [31, 22, 32, 33, 21, 30, 34, 20, 29, 35, 36, 28, 19, 37, 27, 18, 38]
    l_bottom_to_top = [54, 53, 52, 51, 50, 48, 49, 47, 46, 45 ,44, 43]
    i_bottom_to_top = [60, 61, 62, 63]
    o_bottom_to_top = [72, 71, 70, 69, 68, 67]
    t_bottom_to_top = [88, 89, 74, 87, 75, 86, 85, 76, 84, 77, 83, 78, 82, 80, 79, 81]

    line = range(90, 123)

    def __init__(self):
        self.clear()

    def get_array(self):
        return self.arr

    def get_letters(self):
        return [self.a, self.s, self.l, self.i, self.o, self.t]

    def get_line_indexes(self):
        return line

    def get_all_indexes(self):
        return self.get_sign_1() + self.get_sign_2()

    def clear(self):
        self.arr = [0, 0, 0] * 150
