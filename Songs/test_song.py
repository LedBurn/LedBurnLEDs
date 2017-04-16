import pygame

FILE_NAME = "Alan Cortes - Teletubbies (Remix)"
INPUT_FILE = "../Music_Samples/" + FILE_NAME + ".mp3"

import sys, os
sys.path.append(os.path.abspath('../Network'))
import LedBurnProtocol as network
import time
import math

sys.path.append(os.path.abspath('../UIElements'))
from Flower import Flower
flower = Flower()
from SmallSheep import SmallSheep
sheep = SmallSheep()
from Grass import Grass
grass = Grass()
from Sign import Sign
sign = Sign()

sys.path.append(os.path.abspath('../Scenes'))
from RoundRobinScene import RoundRobinScene
scene = RoundRobinScene(flower, sheep, grass, sign)


speed = 25 # in 50 hrz
current_time = 0
frame_id = 0;


#play
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer.music.load(INPUT_FILE)
pygame.mixer.music.play(0, 0)


pieces = [	[0.0,24],
			[10.77405896,16],
			[15.90566893,16],
			[19.34222222,32],
			[22.77877551,32],
			[26.19210884,32],
			[39.91510204, 32]]
current_pieces = 0

frame_id = 0

while pygame.mixer.music.get_busy():
	
	song_time = (pygame.mixer.music.get_pos() - 200)/ 1000.0
	if current_pieces + 1 != len(pieces) and song_time > pieces[current_pieces+1][0]:
		current_pieces += 1

	duration = pieces[current_pieces+1][0] - pieces[current_pieces][0]
	num_of_beats = pieces[current_pieces][1]
	beat_duration = duration/num_of_beats

	relative_song_time = song_time - pieces[current_pieces][0]

	beats_played = math.floor(relative_song_time / beat_duration)
	relative_beat_time = relative_song_time - beat_duration * beats_played
	percent_beat_time = relative_beat_time / beat_duration

	scene.apply(percent_beat_time)
	network.send(frame_id, flower.get_array(), sheep.get_array(), grass.get_array(), sign.get_array())

	clock.tick(20)
	frame_id += 1









