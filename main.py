import datetime
import pygame
from Songs.Song import Song
from Songs.TransitionsDriver import TransitionsDriver
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

transDriver = TransitionsDriver()
song = None
next_song = None
check_num = 0

prevSachiMeter = 0

# uncomment this to start with sensors
from time import sleep
sleep(2)

last_time = 0

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
        song_time = max(song_time, last_time)
        last_time = song_time
        if song.is_transition:
            transDriver.play_animations(curr_temperature, sachiMeter)
        else:
            song.play_animations(song_time, curr_temperature, sachiMeter)

    else: #no song playing
        last_time = 0
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
            next_song = decisions.decide(curr_temperature, sachiMeter, illusionsFlag, motion_detected)

    clock.tick(50)
    




