from AbstractEffect import Effect

import math

class DarkPointEffect(Effect):
    def __init__(self, indexes, num_of_dark):
        """
        :param indexes: 
        :param base_color: 
        :param single_pix_color: 
        :param tot_range_pixels: you can decide that the total number of pixel will be different than len(indexes)
        """
        Effect.__init__(self, indexes)
        self.num_of_dark = num_of_dark

    def apply(self, time_precent, parent_array):
        # dark_index = math.floor((len(self.indexes)+self.num_of_dark*2) * time_precent) - self.num_of_dark
        # start_dark = dark_index - self.num_of_dark/2
        # end_dark = dark_index + self.num_of_dark/2

        # for i in range(len(self.indexes)):
        #     if (i < start_dark or i > end_dark):
        #         dark_percent = 0
        #     else:
        #         dark_percent = (1-math.pow(2*abs(i-dark_index)/self.num_of_dark,2)) * 0.8

        #     color = [int(x * (1-dark_percent)) for x in parent_array[self.indexes[i] * 3: self.indexes[i] * 3 + 3]]
        #     parent_array[self.indexes[i] * 3: self.indexes[i] * 3 + 3] = color

        dark_index = math.floor((len(self.indexes)+self.num_of_dark) * time_precent)
        end_dark = dark_index - self.num_of_dark

        for i in range(len(self.indexes)):
            if (i < end_dark or i > dark_index):
                dark_percent = 0
            else:
                dark_percent = (1-math.pow((dark_index-i)/self.num_of_dark,4)) 

            color = [int(x * (1-dark_percent)) for x in parent_array[self.indexes[i] * 3: self.indexes[i] * 3 + 3]]
            parent_array[self.indexes[i] * 3: self.indexes[i] * 3 + 3] = color




