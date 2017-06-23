import datetime
import pygame
from Songs.Song import Song

clock = pygame.time.Clock()
pygame.mixer.init()

#initialize time vars
MyTime = datetime.datetime.now()
prevTime = MyTime

songs_list = [r'Transitions/post_midburn.yml', 'wish.yml', 'Dreamfunk.yml', 'sheep.yml', 'Soul Orchestra.yml', 'space.yml', 'strawberry.yml', 'TATRAN - Shvat.yml']
next_song_index = 0

song = None

while True:

    MyTime = datetime.datetime.now()

    # current song is playing
    song_playing = song != None and pygame.mixer.music.get_busy()
    if song_playing:
        song_time = (pygame.mixer.music.get_pos())/ 1000.0
        song_time = max(song_time, last_time)
        last_time = song_time
        song.play_animations(song_time, None, None)

    else: #no song playing
        last_time = 0
        next_song = songs_list[next_song_index]
        next_song_index = (next_song_index + 1) % len(songs_list)
        print 'next song is: ' + next_song
        song = Song("Songs/" + next_song)
        pygame.mixer.music.load(song.get_audio_file())
        pygame.mixer.music.play(0, 0)

    clock.tick(50)
    




