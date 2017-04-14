#!/usr/bin/env python

import argparse
import pygame
import librosa
import sys
import os
import ipdb
import numpy as np
import datetime

CLOCK_TICK = 50     # ms

SAMPLE_WINDOW = 500

def fft_buffer(x):
    window = np.hanning(x.shape[0])

    # Calculate FFT
    fx = np.fft.rfft(window * x)

    # Convert to normalised PSD
    Pxx = abs(fx)**2 / (np.abs(window)**2).sum()

    # Scale for one-sided (excluding DC and Nyquist frequencies)
    Pxx[1:-1] *= 2

    # And scale by frequency to get a result in (dB/Hz)
    # Pxx /= Fs
    return Pxx ** 0.5


def draw_bars(screen, s):
 
  for i in xrange(len(s)): 
    erase_rect = (2*i, 10, 2, int(15*30))
    rect = (2*i, 10, 2, int(s[i]*30))
    color = (255, 255, 255)
    pygame.draw.rect(screen, (0,0,0), erase_rect)
    pygame.draw.rect(screen, color, rect)
  

parser = argparse.ArgumentParser()
parser.add_argument("file", help="mp3 file to play",
                    type=str)
args = parser.parse_args()

pygame.init()
clock = pygame.time.Clock()

if not os.path.isfile(args.file):
  print 'file not found: %s' % args.file
  sys.exit(1)

print 'loading %s ...' % args.file
y, sr = librosa.load(args.file)

print 'playtime: %s at sample rate of %d Hz' % (str(datetime.timedelta(0, y.shape[0]/sr)), sr)
pygame.mixer.init()
pygame.mixer.music.load(args.file)
pygame.mixer.music.play(0, 0)

print 'playing: %s' % args.file
#ipdb.set_trace()

width, height = (1200, 600)
screen = pygame.display.set_mode((width, height))

num_frames = y.shape[0]

while pygame.mixer.music.get_busy():
  song_time = pygame.mixer.music.get_pos() / 1000.0  # position in seconds
  
  # calculate frame number
  framenum = song_time * sr

  if framenum < SAMPLE_WINDOW:
    clock.tick(50)
    continue
   
  time_s_window = y[framenum - SAMPLE_WINDOW : framenum] 
  s = fft_buffer(time_s_window)

  draw_bars(screen, s)  
  pygame.display.flip()     # update display with the new drawings

  print 'max: %.3f     min: %.3f' % (s.max(), s.min())
  clock.tick(50)
