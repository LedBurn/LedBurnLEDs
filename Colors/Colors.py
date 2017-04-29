import colorsys
import random
import math

    # def reduce_by_1(x):
    #         while x>=1:
    #             return x-1
    #         return x

    # def opposite_color((r, g, b)):
    #     return [255-r, 255-g, 255-b]

    # def adjacent_color((r, g, b)): # Assumption: r, g, b in [0, 255]
    #     d = 30/360.0
    #     r, g, b = map(lambda x: x/255., [r, g, b]) # Convert to [0, 1]
    #     h, l, s = colorsys.rgb_to_hls(r, g, b)     # RGB -> HLS
    #     h = [(h+d) % 1 for d in (-d, d)]           # Rotation by d
    #     adjacent = [map(lambda x: int(round(x*255)), colorsys.hls_to_rgb(hi, l, s))
    #                 for hi in h] # H'LS -> new RGB
    #     return adjacent

    # def get_random_color():
    #     color = [random.randrange(256), random.randrange(256), random.randrange(256)]
    #     return color

def change_rgb_lightness(rgb_color, lightness_factor):
    return [int(c * lightness_factor) for c in rgb_color]

def fix_lightness_percent(orig_val):
    return orig_val * orig_val

def hsv_to_rgb(h, s, v):
    return [int(c * 255) for c in colorsys.hsv_to_rgb(h, s, v)]

def hls_to_rgb(h, l, s):
    """
    h, l, s - in [0, 1]
    returns [r, g, b] in [0-255]
    """
    return [int(c * 255) for c in colorsys.hsv_to_rgb(h, l, s)]


# def reduce_brightness(color, new_brightness):
#     """
#     color - [r, g, b] in [0-255]
#     new_brightness - in [0, 1]
#     """
#     return [int(c * new_brightness) for c in color]



def go_to_color(fromColor, toColor, percent):
    r = go_to_int(fromColor[0], toColor[0], percent)
    g = go_to_int(fromColor[1], toColor[1], percent)
    b = go_to_int(fromColor[2], toColor[2], percent)
    return [r, g, b]

def go_to_int(fromInt, toInt, percent):
    if (fromInt > toInt):
        diff = fromInt - toInt
        return int(fromInt - diff*percent)
    else:
        diff = toInt - fromInt
        return int(fromInt + diff*percent)


def gradient_array(fromColor, toColor, num_of_leds, power=1):
    colors = []
    for i in range(num_of_leds):
        percent = float(i)/num_of_leds
        percent = math.pow(percent, power)
        color = go_to_color(fromColor, toColor, percent)
        colors = colors + color

    return colors


