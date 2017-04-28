import sys, os
sys.path.append(os.path.abspath('../'))

import pygame
from Song import Song

song = Song("TATRAN - Shvat.yml")

clock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer.music.load("../" + song.get_audio_file())
pygame.mixer.music.play(0, 0)

while pygame.mixer.music.get_busy():
    song_time = pygame.mixer.music.get_pos() / 1000.0
    song.play_animations(song_time, None)
    clock.tick(50)