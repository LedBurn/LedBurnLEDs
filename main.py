import time
import datetime
import pygame
import socket
from Songs.Song import Song
from Sensors.RFID import RFID
from Sensors.Temperature import Temperature
from Sensors.Motion import Motion

r = RFID()
temperature = Temperature()
motion = Motion()

clock = pygame.time.Clock()
pygame.mixer.init()

#initialize time vars
MyTime = datetime.datetime.now()
prevTime = MyTime
rfidTime = MyTime

song = Song("Songs/Teletubbies.yml")
pygame.mixer.music.load(song.get_audio_file())
pygame.mixer.music.play(0, 0)
check_num = 0

start_temp = None
prevSachiMeter = 0


while True:
	# read sensors data
	# todo - sample motion & temp sensors - by udp
	#  

	MyTime = datetime.datetime.now()

	sachiMeter, illusionsFlag = r.process()
	curr_temperature = temperature.get_temperature()

	# if (MyTime.second != prevTime.second):
		# print MyTime.second-prevTime.second


	# current song is playing
	if song != None and pygame.mixer.music.get_busy():
		sont_time = (pygame.mixer.music.get_pos() - 170)/ 1000.0
		song.play_animations(sont_time, curr_temperature)
		start_temp = curr_temperature

	# new song
	else:
		# to do - decide which song, maybe a break?
		# white glow animation
		# check sensors in 10 seconds intervals
		if ((MyTime-prevTime)>datetime.timedelta(seconds=10)):
			check_num += 1
			prevTime = MyTime
			# if temperature delta in 10 seconds is more than 2 degrees, someone is touching
			if start_temp is not None and curr_temperature is not None and (curr_temperature-start_temp)>2:
				print "thanks for the hug, play a hippie song"
				# song = Song("Songs/Soul Orchestra.yml")
				# song = Song("Songs/Dreamfunk.yml")
				song = Song("Songs/Teletubbies.yml")
				pygame.mixer.music.load(song.get_audio_file())
				pygame.mixer.music.play(0, 0)
				break

			if (curr_temperature is not None and curr_temperature < 20):
				print "my branch is a little cold, any tree huggers to the rescue?"
			elif (curr_temperature is not None and curr_temperature > 28):
				print "its so warm, somebody must be hugging me, play a hippie song"
				# song = Song("Songs/Soul Orchestra.yml")
				song = Song("Songs/Dreamfunk.yml")
				# song = Song("Songs/Teletubbies.yml")
				pygame.mixer.music.load(song.get_audio_file())
				pygame.mixer.music.play(0, 0)
			elif (sachiMeter > 2):
				print "Wow ani patzutz, I need a song to relax (play a chill song)"
			elif (sachiMeter-prevSachiMeter):
				print "I need another Sachta"
			elif (sachiMeter < -2):
				print "Oh man, i better stretch these old bones, lets get the beat going! (play upbeat song)"
			elif(prevSachiMeter-sachiMeter):
				print "Hmm.. havent been to the gym in a while.. i need to go some time"
			# SachiMeter at 0 is default, maybe illusions audio shouldnt be at default?
			elif (illusionsFlag):
				IllusionFlag = False
				print "Hi, welcome to the Illusions led mirage, sometimes we all need a reminder that Illusions look very real, so much that we practically live them, what are yours? (play *illusions* audio)"
			
			# update prev vars
			start_temp = curr_temperature
			prevSachiMeter = sachiMeter
		elif (check_num == 3):
			check_num = 0
			prevTime = MyTime
			print "no decision by sensors, pick random song"
		# else:
			# white glow animation


	clock.tick(50)
	




