import colorsys
import random

def reduce_by_1(x):
        while x>=1:
            return x-1
        return x

def opposite_color((r, g, b)):
    return [255-r, 255-g, 255-b]

def adjacent_color((r, g, b)): # Assumption: r, g, b in [0, 255]
    d = 30/360.0
    r, g, b = map(lambda x: x/255., [r, g, b]) # Convert to [0, 1]
    h, l, s = colorsys.rgb_to_hls(r, g, b)     # RGB -> HLS
    h = [(h+d) % 1 for d in (-d, d)]           # Rotation by d
    adjacent = [map(lambda x: int(round(x*255)), colorsys.hls_to_rgb(hi, l, s))
                for hi in h] # H'LS -> new RGB
    return adjacent

def get_random_color():
    color = [random.randrange(256), random.randrange(256), random.randrange(256)]
    return color
