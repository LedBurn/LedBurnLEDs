import sys
import yaml
import colorsys

# Model Helpers. 

# loads a led model
# for now represented by a simple .yml file
def load_model(model_file):
  model = {}
  with open(model_file, 'r') as stream:
    model = yaml.load(stream)
  
  return model



# returns a physical model normalized to a starting point of (0, 0)
def get_normalized_model(physical_mapping):
  
  # find minimum x,y values for screen size calculation
  x_min, y_min = sys.maxint, sys.maxint
  for x,y in physical_mapping:
    x_min = min(x_min, x)
    y_min = min(y_min, y)
  
  normalized_mapping = [None] * len(physical_mapping)
  for i in xrange(len(physical_mapping)):
    x, y = physical_mapping[i]
    normalized_mapping[i] = [x - x_min, y - y_min] 

  return normalized_mapping



def generate_rainbow(length, cycle, offset=0):
  ''' generate rainbow pattern by cycling over all hues in the HSV color space'''
  rainbow = []
  
  for i in xrange(length):
    phase = (i + offset) % cycle
    h = float(phase) / cycle
    rgb = colorsys.hsv_to_rgb(h, 1.0, 1.0) 

    # convert to uint8 type values
    rgb = [int(value * 255) for value in rgb]
    rainbow.append(tuple(rgb))

  return rainbow



