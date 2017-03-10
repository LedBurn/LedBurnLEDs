import modelutils



class Model(object):
  ''' This class represents a basic model. '''

  # default color of a model
  DEFAULT_COLOR = (0, 0, 0)


  def __init__(self, model_file):
    self.model = modelutils.load_model(model_file)
    
    self.physical_mapping = self.model['physical_mapping']
    
    # color values of the model
    # default is initialized to all white
    # colors are represented as (R,G,B) tuples with values of [0..255]
    self.colors = [self.DEFAULT_COLOR for i in xrange(len(self.physical_mapping))]

    # normalize model physical representation
    self.physical_mapping = modelutils.get_normalized_model(self.physical_mapping)

  
 
  def number_of_leds(self):
    '''returns the number of leds the in the led model. '''
    return len(self.physical_mapping)



  def dimensions(self):
    '''returns the width, height of a bounding rectangle.'''

    x_max, y_max = 0, 0
    for xy_position in self.physical_mapping:
      if xy_position is None:
        continue
      x, y = xy_position
      x_max = max(x_max, x)
      y_max = max(y_max, y)

    width, height = x_max + 1, y_max + 1
    return (width, height) 



  def set_led_color(self, index, color):
    '''set color for a specific led by index'''

    if index >= len(self.physical_mapping):
      raise ValueError('index out of bounds')
    
    if not (isinstance(color, tuple) and len(color) == 3):
      raise ValueError('invalid color value or type')

    self.colors[index] = color
    return self



  def set_colors(self, pattern, **kwargs):
    '''set color pattern for all leds'''
    
    if pattern == 'uniform':
      if 'color' not in kwargs:
        raise ValueError('color is a required parameter')

      for i in xrange(len(self.colors)):
        self.set_led_color(i, kwargs['color'])
    
    elif pattern == 'rainbow':
      if 'cycle' in kwargs:
        cycle = kwargs['cycle']
      else:
        cycle = len(self.colors)    

      self.colors = modelutils.generate_rainbow(len(self.colors), cycle)

    else:
      raise ValueError('unsupported pattern')

    return self

