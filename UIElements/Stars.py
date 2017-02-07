

class Stars:

    def __init__(self):
        self.clear()
        
    def get_array(self):
        return self.arr

    def get_all_indexes(self):
        return range(0,300)

    def num_of_stars(self):
        return 300
        
    def clear(self):
        self.arr = [0, 0, 0] * self.num_of_stars()