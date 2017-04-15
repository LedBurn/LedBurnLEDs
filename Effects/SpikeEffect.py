from AbstractEffect import Effect


class SpikeEffect(Effect):
    def __init__(self, indexes, base_color, tail_percent, tot_range_pixels):
        """
        :param indexes: 
        :param base_color: 
        :param tail_percent: out of the tot_range_pixels 
        :param tot_range_pixels: you can decide that the total number of pixel will be different than len(indexes)
        """
        Effect.__init__(self, indexes)
        self.base_color = base_color
        self.tail_percent = tail_percent
        self.tot_range_pixels = tot_range_pixels
        self.tot_pixel_with_tail = (1 + tail_percent) * tot_range_pixels

    def apply(self, time_precent, parent_array):
        top_pixel = self.tot_pixel_with_tail * time_precent
        bottom_pixel = top_pixel - self.tot_range_pixels * self.tail_percent

        for i in range(0, len(self.indexes)):
            color = [0, 0, 0]
            if i >= bottom_pixel and i <= top_pixel:
                i_percent = float(i - bottom_pixel) / float(top_pixel - bottom_pixel)
                color = [int(c * i_percent) for c in self.base_color]
            index_in_obj = self.indexes[i]
            parent_array[index_in_obj * 3: index_in_obj * 3 + 3] = color




