import time
import datetime
import MFRC522
import pygame
import socket
from Songs.Song import Song

clock = pygame.time.Clock()
pygame.mixer.init()


# temp sensor
tempUDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
temperature_listen_addr = ("",5005)
tempUDPSock.bind(temperature_listen_addr)
tempUDPSock.setblocking(0)
start_temp = -127
temperature = -127

# motion sensor
motionUDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
motion_listen_addr = ("",5006)
motionUDPSock.bind(motion_listen_addr)
motionUDPSock.setblocking(0)
motionAccum = 0

#RFID sensor
# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()
gymUID = [236,237,86,75]
jointUID = [32,230,68,223]
cardUID = [21,211,122,69]
SachiMeter = 0
prevSachiMeter = 0
illusionFlag = False

#initialize time vars
MyTime = datetime.datetime.now()
prevTime = MyTime
rfidTime = MyTime

song = None
check_num = 0


def ReadNonBlockingUDP(UDPSock):
	try:
		data, addr = UDPSock.recvfrom(1024)
		#print data.strip(), addr
		return float(data.strip())
	except:
		return -127


def RFIDRead():
	# Scan for cards
	(status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

	# If a card is found
	if status == MIFAREReader.MI_OK:
		print "Card detected"
	else:
		return [0,0,0,0]

	# Get the UID of the card
	(status, uid) = MIFAREReader.MFRC522_Anticoll()
	
	# If we have the UID, continue
	if status == MIFAREReader.MI_OK:
		return uid[0:4]
	else:
		return [0,0,0,0]
		
		# Print UID
		#print "Card read UID: " + str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3])
		# if ((uid[0]==Desired_UID[0]) & (uid[1]==Desired_UID[1]) & (uid[2]==Desired_UID[2]) & (uid[3]==Desired_UID[3])):
			# return 1
		# else:
			# return 0


while True:
	# read sensors data
	# todo - sample motion & temp sensors - by udp
	#  
	tempRead = ReadNonBlockingUDP(tempUDPSock)
	if (tempRead != -127):
		temperature = tempRead
		print tempRead
		# adjust temp meter leds to reflect new temperature

	motionRead = ReadNonBlockingUDP(motionUDPSock)
	if (motionRead != -127):
		motionAccum += motionRead
		print motionAccum
	
	whichUID = RFIDRead()
	if (set(whichUID) == set(jointUID)):
		#print "ID MATCH!"
		# 3 seconds between detections avoids redundant consequtive detections
		if ((MyTime-rfidTime)>datetime.timedelta(seconds=3)):
			rfidTime = MyTime
			if (SachiMeter<4):
				SachiMeter += 1
			print "SachiMeter at " + str(SachiMeter)
	elif (set(whichUID) == set(gymUID)):
		if ((MyTime-rfidTime)>datetime.timedelta(seconds=3)):
			rfidTime = MyTime
			if (SachiMeter>-4):
				SachiMeter += -1
			print "SachiMeter at " + str(SachiMeter)
	elif (set(whichUID) == set(cardUID)):
		if ((MyTime-rfidTime)>datetime.timedelta(seconds=3)):
			rfidTime = MyTime
			SachiMeter = 0
			illusionFlag = True
	else:
		if ((MyTime-rfidTime)>datetime.timedelta(seconds=30)):
			rfidTime = MyTime
			if (SachiMeter>0):
        			SachiMeter -= 1
			elif (SachiMeter<0):
					SachiMeter += 1
			print "SachiMeter at " + str(SachiMeter)
	
	MyTime = datetime.datetime.now()
	
	# if (MyTime.second != prevTime.second):
		# print MyTime.second-prevTime.second


	# current song is playing
	if song != None and pygame.mixer.music.get_busy():
		song.play_animations((pygame.mixer.music.get_pos() - 170)/ 1000.0)
		start_temp = temperature

	# new song
	else:
		# to do - decide which song, maybe a break?
		# white glow animation
		# check sensors in 10 seconds intervals
		if ((MyTime-prevTime)>datetime.timedelta(seconds=10)):
			check_num += 1
			prevTime = MyTime
			# if temperature delta in 10 seconds is more than 2 degrees, someone is touching
			if (((temperature-start_temp)>2) & (start_temp>0)):
				print "thanks for the hug, play a hippie song"
				# song = Song("Songs/Soul Orchestra.yml")
				# song = Song("Songs/Dreamfunk.yml")
				song = Song("Songs/Teletubbies.yml")
				pygame.mixer.music.load(song.get_audio_file())
				pygame.mixer.music.play(0, 0)
				break

			if (temperature < 20):
				print "my branch is a little cold, any tree huggers to the rescue?"
			elif (temperature > 28):
				print "its so warm, somebody must be hugging me, play a hippie song"
				# song = Song("Songs/Soul Orchestra.yml")
				song = Song("Songs/Dreamfunk.yml")
				# song = Song("Songs/Teletubbies.yml")
				pygame.mixer.music.load(song.get_audio_file())
				pygame.mixer.music.play(0, 0)
			elif (SachiMeter > 2):
				print "Wow ani patzutz, I need a song to relax (play a chill song)"
			elif (SachiMeter-prevSachiMeter):
				print "I need another Sachta"
			elif (SachiMeter < -2):
				print "Oh man, i better stretch these old bones, lets get the beat going! (play upbeat song)"
			elif(prevSachiMeter-SachiMeter):
				print "Hmm.. havent been to the gym in a while.. i need to go some time"
			# SachiMeter at 0 is default, maybe illusions audio shouldnt be at default?
			elif (illusionFlag):
				IllusionFlag = False
				print "Hi, welcome to the Illusions led mirage, sometimes we all need a reminder that Illusions look very real, so much that we practically live them, what are yours? (play *illusions* audio)"
			
			# update prev vars
			start_temp = temperature
			prevSachiMeter = SachiMeter
		elif (check_num == 3):
			check_num = 0
			prevTime = MyTime
			print "no decision by sensors, pick random song"
		# else:
			# white glow animation


	clock.tick(50)
	




