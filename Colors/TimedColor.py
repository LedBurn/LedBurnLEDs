"""
This module can produce a color that changes over time.
Effects and animations can then be configured with complex color models by suplling a single instance
"""

from abc import ABCMeta, abstractmethod

import Colors


class AbstractTimedColor:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_color(self, time_percent, location_percent): pass
    def get_hue(self, time_percent, location_percent): pass

class ConstTimedColor(AbstractTimedColor):

    def __init__(self, rgb_color):
        AbstractTimedColor.__init__(self)
        self.rgb_color = rgb_color

    def get_color(self, time_percent, location_percent):
        return self.rgb_color

    def get_hue(self, time_percent, location_percent):
        return 0

class HueChangeTimedColor(AbstractTimedColor):

    def __init__(self, hue_start, hue_end):
        AbstractTimedColor.__init__(self)
        self.hue_start = hue_start
        self.hue_end = hue_end
        self.hue_diff = hue_end - hue_start

    def get_color(self, time_percent, location_percent):
        return Colors.hls_to_rgb(self.get_hue(time_percent, location_percent), 1.0, 1.0)

    def get_hue(self, time_percent, location_percent):
        curr_hue = self.hue_start + self.hue_diff * time_percent
        while curr_hue < 0:
            curr_hue += 1
        while curr_hue > 1:
            curr_hue -= 1
        return curr_hue;

class CircularLocHue(AbstractTimedColor):

    def __init__(self):
        AbstractTimedColor.__init__(self)

    def get_color(self, time_percent, location_percent):
        return Colors.hls_to_rgb(location_percent, 1.0, 1.0)


class HueChangeTimedColorByLocation(AbstractTimedColor):

    def __init__(self, hue_start, hue_end):
        AbstractTimedColor.__init__(self)
        self.hue_start = hue_start
        self.hue_end = hue_end
        self.hue_diff = hue_end - hue_start

    def get_color(self, time_percent, location_percent):
        return Colors.hls_to_rgb(self.get_hue(time_percent, location_percent), 1.0, 1.0)

    def get_hue(self, time_percent, location_percent):
        curr_hue = self.hue_start + self.hue_diff * location_percent
        while curr_hue < 0:
            curr_hue += 1
        while curr_hue > 1:
            curr_hue -= 1
        return curr_hue;


def TimedColorFactory(props):

    if 'type' not in props:
        print 'expect property type in color configuration: ' + str(props)
        return None

    color_type = props['type']
    if color_type == "circular_loc_hue":
        return CircularLocHue()
    elif color_type == "hue_change_time":
        if "hue_start" not in props or "hue_end" not in props:
            print "missing 'hue_start' or 'hue_end' in " + str(props) + " for color of type " + color_type
            return None
        return HueChangeTimedColor(props["hue_start"], props["hue_end"])
    elif color_type == "const_color":
        if "hue" not in props:
            print "missing 'hue' in " + str(props) + " for color of type " + color_type
            return None
        sat = 1.0 if "sat" not in props else props["sat"]
        val = 1.0 if "val" not in props else props["val"]
        return ConstTimedColor(Colors.hsv_to_rgb(props["hue"], sat, val))
    elif color_type == "timed_hue":
        if "hue_start" not in props or "hue_end" not in props:
            print "missing 'hue_start' or 'hue_end' in " + str(props) + " for color of type " + color_type
            return None
        return HueChangeTimedColor(props["hue_start"], props["hue_end"])

    print 'cannot find color with type ' + str(color_type)


