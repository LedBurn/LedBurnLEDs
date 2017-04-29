from AbstractEffect import Effect

from Colors import Colors

class SpikeEffect(Effect):
    def __init__(self, indexes, timed_color, tail_percent, tot_range_pixels, circular=False):
        """
        :param indexes: 
        :param base_color: 
        :param tail_percent: out of the tot_range_pixels 
        :param tot_range_pixels: you can decide that the total number of pixel will be different than len(indexes)
        """
        Effect.__init__(self, indexes)
        self.timed_color = timed_color
        self.tail_percent = tail_percent
        self.tot_range_pixels = tot_range_pixels
        self.tot_pixel_with_tail = tot_range_pixels if circular else (1 + tail_percent) * tot_range_pixels
        self.circular = circular

    def apply(self, time_percent, parent_array):
        top_pixel = self.tot_pixel_with_tail * time_percent
        bottom_pixel = top_pixel - self.tot_range_pixels * self.tail_percent

        for i in range(0, len(self.indexes)):
            color = self.get_color(time_percent, top_pixel, bottom_pixel, i)
            index_in_obj = self.indexes[i]
            parent_array[index_in_obj * 3: index_in_obj * 3 + 3] = color

    def get_color(self, time_percent, top_pixel, bottom_pixel, i):
        color = self.get_color_for_index(time_percent, top_pixel, bottom_pixel, i)
        if color is not None:
            return color
        if self.circular:
            color = self.get_color_for_index(time_percent, top_pixel, bottom_pixel, i + len(self.indexes))
            if color is not None:
                return color
            color = self.get_color_for_index(time_percent, top_pixel, bottom_pixel, i - len(self.indexes))
            if color is not None:
                return color
        return [0,0,0] # default is black


    def get_color_for_index(self, time_percent, top_pixel, bottom_pixel, i):
        if i >= bottom_pixel and i <= top_pixel:
            i_percent = float(i - bottom_pixel) / float(top_pixel - bottom_pixel)
            return Colors.change_rgb_lightness(self.timed_color.get_color(time_percent, i_percent),
                                                Colors.fix_lightness_percent(i_percent))
        return None





