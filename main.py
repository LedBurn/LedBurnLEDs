import time
import datetime
# import MFRC522
import pygame
import socket
from Songs.Song import Song

clock = pygame.time.Clock()
pygame.mixer.init()

start_temp = 127

# temp sensor
tempUDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
temperature_listen_addr = ("",5005)
tempUDPSock.bind(temperature_listen_addr)
tempUDPSock.setblocking(0)

# motion sensor
motionUDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
motion_listen_addr = ("",5006)
motionUDPSock.bind(motion_listen_addr)
motionUDPSock.setblocking(0)

#RFID sensor
# Create an object of the class MFRC522
# MIFAREReader = MFRC522.MFRC522()

#initialize time vars
MyTime = datetime.datetime.now()
prevTime = MyTime
rfidTime = MyTime

song = None



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
		return -1

	# Get the UID of the card
	(status, uid) = MIFAREReader.MFRC522_Anticoll()
	
	# If we have the UID, continue
	if status == MIFAREReader.MI_OK:
	
		# Print UID
		print "Card read UID: " + str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3])
	
		# This is the default key for authentication
		key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
	
		# Select the scanned tag
		MIFAREReader.MFRC522_SelectTag(uid)
	
		# Authenticate
		status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
	
		# Check if authenticated
		if status == MIFAREReader.MI_OK:
			MIFAREReader.MFRC522_Read(8)
			MIFAREReader.MFRC522_StopCrypto1()
		else:
			print "Authentication error"


while True:
	# read sensors data
	# todo - sample motion & temp sensors - get udp?
	#  
	tempRead = ReadNonBlockingUDP(tempUDPSock)
	if (tempRead != -127):
		temperature = tempRead
		print tempRead
		# adjust temp meter leds to reflect new temperature

	motionRead = ReadNonBlockingUDP(motionUDPSock)
	if (motionRead != -127):
		print motionRead
	
	# need to think how to avoid consequtive detections
	# whichRFID = RFIDRead()
	# if (whichRFID == 1):
		# print "ID is the joint"
		# if ((MyTime-rfidTime)>datetime.timedelta(seconds=3)):
			# rfidTime = MyTime
			# SachiMeter += 1
	
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
		# check temperature in 10 seconds intervals
		if ((MyTime-prevTime)>datetime.timedelta(seconds=10)):
			prevTime = MyTime
			# if temperature delta in 10 seconds is more than 2 degrees, someone is touching
			if ((temperature-start_temp)>2):
				print "thanks for the hug, play a hippie song"
				# song = Song("Songs/Soul Orchestra.yml")
				# song = Song("Songs/Dreamfunk.yml")
				song = Song("Songs/Teletubbies.yml")
				pygame.mixer.music.load(song.get_audio_file())
				pygame.mixer.music.play(0, 0)

			start_temp = temperature
			if (temperature < 26):
				print "i'm a little cold, can somebody hug me?"
			elif (temperature > 28):
				print "its so warm, somebody must be hugging me, play a hippie song"
				# song = Song("Songs/Soul Orchestra.yml")
				song = Song("Songs/Dreamfunk.yml")
				# song = Song("Songs/Teletubbies.yml")
				pygame.mixer.music.load(song.get_audio_file())
				pygame.mixer.music.play(0, 0)
			
		# else:
			# white glow animation


	clock.tick(50)
	




