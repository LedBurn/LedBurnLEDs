#!/usr/bin/env python

import argparse
import pygame
import librosa
import sys
import os
import ipdb

parser = argparse.ArgumentParser()
parser.add_argument("file", help="mp3 file to play",
                    type=str)
args = parser.parse_args()

pygame.init()
clock = pygame.time.Clock()

if not os.path.isfile(args.file):
  print 'file not found: %s' % args.file
  sys.exit(1)

print 'loading %s for audio analysis' % args.file
y, sr = librosa.load(args.file)

print 'running beat tracker'
onset_env = librosa.onset.onset_strength(y, sr=sr)
y_percussive = librosa.effects.hpss(y)
tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, onset_envelope=onset_env, sr=sr)
print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

pygame.mixer.init()
pygame.mixer.music.load(args.file)
pygame.mixer.music.play(0, 0)

print 'playing: %s' % args.file

next_beat_idx = 0

while pygame.mixer.music.get_busy():
  song_time = pygame.mixer.music.get_pos() / 1000.0  # position in seconds
  #print 'song time: %f, next beat: %f' % (song_time, beat_times[next_beat_idx])
  if next_beat_idx == len(beat_times):
    print 'no more beats'
    sys.exit() 
  
  if beat_times[next_beat_idx] <= song_time:
    print 'beat at: %f' % beat_times[next_beat_idx]
    next_beat_idx += 1 

  clock.tick(20)
