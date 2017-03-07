#!/usr/bin/env python

'''
Utility to view a model.
Assumes simple .yml (no parsing yet..)
'''

import os
import sys
import pygame
import yaml
import argparse
import ipdb


#################################################
# Constants for viewing the model
# TODO: move to configuration file
PIXEL_SIZE = 6


# draws model according to a list of physical [x, y] mapping on a plane  
def draw_model(screen, physical_mapping):

  for x, y in physical_mapping:
    rect = [PIXEL_SIZE * x, PIXEL_SIZE * y, PIXEL_SIZE, PIXEL_SIZE] 
    pygame.draw.rect(screen, [255, 255, 255], rect)



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



def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("file", help="model file to view",
                      type=str)
  args = parser.parse_args()

  if not os.path.isfile(args.file):
    print 'file not found: %s' % args.file
    sys.exit(1)

  model = {}
  with open(args.file, 'r') as stream:
    model = yaml.load(stream)

  physical_mapping = get_normalized_model(model['physical_mapping'])


  # find maximum x,y values for screen size calculation
  x_max, y_max = 0, 0
  for x,y in physical_mapping:
    x_max = max(x_max, x)
    y_max = max(y_max, y)

  width, height = x_max + 1, y_max + 1

  size = [PIXEL_SIZE * width, PIXEL_SIZE * height]

  # initialize display
  screen = pygame.display.set_mode(size)
  
  draw_model(screen, physical_mapping)
  pygame.display.flip()     # update display with the new drawings
  
  clock = pygame.time.Clock()
  
  # display loop
  while True:
    clock.tick(50)

    for event in pygame.event.get():  # user did something
      if event.type == pygame.QUIT:
        return
    


if __name__ == '__main__':
  main()
