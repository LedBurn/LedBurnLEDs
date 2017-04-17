import pygame
import socket
from Songs.Song import Song

clock = pygame.time.Clock()
pygame.mixer.init()



# temp sensor
# UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# listen_addr = ("",5005)
# UDPSock.bind(listen_addr)


song = None

while True:
	# read sensors data
	# todo - sample motion & temp sensors - get udp?
	#  
	# data, addr = UDPSock.recvfrom(1024)
	# print data.strip(), addr


	# current song is playing
	if song != None and pygame.mixer.music.get_busy():
		song.play_animations((pygame.mixer.music.get_pos() - 170)/ 1000.0)

	# new song
	else:
		# to do - decide which song, maybe a break?
		# song = Song("Songs/Soul Orchestra.yml")
		song = Song("Songs/Dreamfunk.yml")
		pygame.mixer.music.load(song.get_audio_file())
		pygame.mixer.music.play(0, 0)


	clock.tick(50)
	




