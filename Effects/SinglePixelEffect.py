from AbstractEffect import Effect


class SinglePixelEffect(Effect):
    def __init__(self, indexes, base_color, single_pix_color, tot_range_pixels):
        """
        :param indexes: 
        :param base_color: 
        :param single_pix_color: 
        :param tot_range_pixels: you can decide that the total number of pixel will be different than len(indexes)
        """
        Effect.__init__(self, indexes)
        self.base_color = base_color
        self.single_pix_color = single_pix_color
        self.tot_range_pixels = tot_range_pixels

    def apply(self, time_precent, parent_array):
        for i in self.indexes:
            parent_array[i * 3: i * 3 + 3] = self.base_color
        pix_i_to_paint = int(self.tot_range_pixels * time_precent)
        if pix_i_to_paint < len(self.indexes):
            index_in_obj = self.indexes[pix_i_to_paint]
            parent_array[index_in_obj * 3: index_in_obj * 3 + 3] = self.single_pix_color




