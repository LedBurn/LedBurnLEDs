#!/usr/bin/env python

import sys, os

sys.path.append(os.path.abspath('../Network'))
import LedBurnProtocol as network
import time

sys.path.append(os.path.abspath('../UIElements'))
from Grass import Grass

grass = Grass()

INPUT_FILE = "/home/amir/Downloads/PingPong.mp3"
LABELS_FILE = "/home/amir/Beats.txt"

from RoundRobinGrassAnimation import RoundRobinGrassAnimation
with open(LABELS_FILE, "r") as f:
    beats = [ float(a.split()[0]) for a in f.readlines()]
beats_total_time = beats[-1]
beats_percent = [b / beats_total_time for b in beats]
animation = RoundRobinGrassAnimation(grass, beats_percent)

flower = [0, 0, 0] * 550
sheep = [0, 0, 0] * 302
sign = [0, 0, 0] * 150

speed = 25  # in 50 hrz
current_time = 0
frame_id = 0;


import pygame

pygame.mixer.init()
pygame.mixer.music.load(INPUT_FILE)
pygame.mixer.music.play(0, 0)
pygame.init()
clock = pygame.time.Clock()

i = 0
last_time = 0

while pygame.mixer.music.get_busy():
    song_time = pygame.mixer.music.get_pos()
    song_time = (song_time - 200) / 1000.0
    last_time = song_time
    i += 1

    time_precent = float(song_time) / beats_total_time
    animation.apply(time_precent)

    network.send(flower, sheep, grass.get_array(), sign)
    frame_id += 1

    clock.tick(50)


