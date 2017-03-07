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
from model import Model


#################################################
# Constants for viewing the model
# TODO: move to configuration file
PIXEL_SIZE = 6


# draws model according to a list of physical [x, y] mapping on a plane  
def draw_model(screen, physical_mapping, colors):

  for i in xrange(len(physical_mapping)):
    x, y = physical_mapping[i]
    color = colors[i]
    rect = [PIXEL_SIZE * x, PIXEL_SIZE * y, PIXEL_SIZE, PIXEL_SIZE] 
    pygame.draw.rect(screen, color, rect)



def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("file", help="model file to view",
                      type=str)
  args = parser.parse_args()

  m = Model(args.file)

  # determine screen size
  width, height = m.dimensions()
  size = [PIXEL_SIZE * width, PIXEL_SIZE * height]

  # initialize display
  screen = pygame.display.set_mode(size)
  
  m.set_colors('rainbow') 
  draw_model(screen, m.physical_mapping, m.colors)
  pygame.display.flip()     # update display with the new drawings
  
  
  # display loop
  clock = pygame.time.Clock()
  while True:
    clock.tick(50)

    for event in pygame.event.get():  # user did something
      if event.type == pygame.QUIT:
        return
    


if __name__ == '__main__':
  main()
