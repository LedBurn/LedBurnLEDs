import time
import datetime
import pygame
import socket
from Songs.Song import Song
from Sensors.RFIDUDP import RFIDUDP
from Sensors.Temperature import Temperature
from Sensors.Motion import Motion
from Sensors.Decisions import Decisions

rf = RFIDUDP()
temperature = Temperature()
motion = Motion()
decisions = Decisions()

clock = pygame.time.Clock()
pygame.mixer.init()

#initialize time vars
MyTime = datetime.datetime.now()
prevTime = MyTime
rfidTime = MyTime

song = None
next_song = None
check_num = 0

start_temperature = None
prevSachiMeter = 0

# uncomment this to start with sensors
#from time import sleep
#sleep(2)

while True:
    # read sensors data
    # todo - sample motion & temp sensors - by udp
    #  

    MyTime = datetime.datetime.now()

    sachiMeter, illusionsFlag = rf.process()
    curr_temperature = temperature.get_temperature()
    motion_detected = motion.get_has_motion()

    # current song is playing
    song_playing = song != None and pygame.mixer.music.get_busy()
    if song_playing:
        song_time = (pygame.mixer.music.get_pos())/ 1000.0
        song.play_animations(song_time, curr_temperature, sachiMeter)
        start_temperature = curr_temperature
    else: #no song playing
        if next_song is not None:
            print "next song is: " + next_song[0]
            song = Song("Songs/" + next_song[0])
            pygame.mixer.music.load(song.get_audio_file())
            pygame.mixer.music.play(0, 0)
            if len(next_song) > 1:
                del next_song[0]
            else:
                next_song = None
        else:
            next_song = decisions.decide(start_temperature, curr_temperature, sachiMeter, illusionsFlag, motion_detected)

    clock.tick(50)
    




