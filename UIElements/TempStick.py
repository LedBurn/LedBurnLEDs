
import datetime

from Effects.SpikeEffect import SpikeEffect
from Colors.TimedColor import ConstTimedColor

class TempStick:

    MAX_TEMP = 32.0
    MIN_TEMP = 15.0

    NUM_OF_PIX = 144
    MID_PIX = NUM_OF_PIX / 2.0

    SAMPLES_FOR_CHANGE_DETECTION = 10
    DEG_DIFF_FOR_CHANGE_DETECTION = 0.3

    top_pixels = range(120,144)

    def __init__(self):
        self.arr = [0,0,0] * self.NUM_OF_PIX
        self.is_on = False
        self.brightness = 1.0
        self.last_samples = []
        self.last_sample_time = datetime.datetime.now()
        self.is_input_mode = False
        self.top_spike = None

    def get_array(self):
        return self.arr

    def set_temperature(self, time_percent, curr_temp):

        self.change_detection(curr_temp)

        if curr_temp is None or self.is_on is False:
            self.all_same_color([0,0,0])
        else:
            curr_temp = max(curr_temp, self.MIN_TEMP)
            curr_temp = min(curr_temp, self.MAX_TEMP)
            temp_percent = (curr_temp - self.MIN_TEMP)/(self.MAX_TEMP - self.MIN_TEMP)
            pix_num = int(temp_percent * self.NUM_OF_PIX)

            if pix_num >= self.NUM_OF_PIX:
                self.all_same_color([255, 0, 0])
            elif pix_num <= 0:
                self.all_same_color([0,0,255])
            else:
                for i in range(0, self.NUM_OF_PIX):
                    r = 0
                    b = 0
                    if i < pix_num:
                        if i < self.MID_PIX:
                            b = int( self.brightness * 255 * (1.0- i / self.MID_PIX))
                        else:
                            r = int( self.brightness * 255 * ( float(i-self.MID_PIX) / float(self.MID_PIX) ))
                    self.arr[i*3 : i*3+3] = [r, 0, b]

            if self.top_spike:
                self.top_spike.apply(time_percent, self.arr)

    def change_detection(self, curr_temp):

        if (datetime.datetime.now() - self.last_sample_time) < datetime.timedelta(seconds=1):
            return
        self.last_sample_time = datetime.datetime.now()

        if curr_temp is None:
            self.last_samples = []
        else:
            if len(self.last_samples) > self.SAMPLES_FOR_CHANGE_DETECTION:
                diff_for_window = curr_temp - self.last_samples[0]
                if diff_for_window > self.DEG_DIFF_FOR_CHANGE_DETECTION:
                    self.set_is_on(True)
                del self.last_samples[0]
            self.last_samples.append(curr_temp)

    def all_same_color(self, color):
        for i in range(0, 144):
            self.arr[i*3 : i*3+3] = color

    def set_brightness(self, val):
        self.brightness = val

    def set_is_on(self, val):
        self.is_on = val

    def set_is_input_mode(self, val):
        if self.is_input_mode == val:
            return
        if val:
            self.top_spike = SpikeEffect(self.top_pixels, ConstTimedColor([255, 0, 0]), 1.0, len(self.top_pixels), False)
        else:
            self.top_spike = None
        self.is_input_mode = val



