import sys, os
sys.path.append(os.path.abspath('../'))

import pygame
from Song import Song

song = Song("strawberry.yml")

clock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer.music.load("../" + song.get_audio_file())
pygame.mixer.music.play(0, 0)
last_song_time = 0

while pygame.mixer.music.get_busy():
    song_time = pygame.mixer.music.get_pos() / 1000.0
    if song_time > last_song_time:
        last_song_time = song_time
    song.play_animations(last_song_time, None)
    clock.tick(50)