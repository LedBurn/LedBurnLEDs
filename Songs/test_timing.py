import sys, os
sys.path.append(os.path.abspath('../'))

import Network.LedBurnProtocol as network
import time
import math
import pygame
import yaml

from UIElements.Flower import Flower
from UIElements.SmallSheep import SmallSheep
from UIElements.Grass import Grass
from UIElements.Sign import Sign
from UIElements.Lake import Lake

from Colors import Colors

FILE = 'TATRAN - Shvat.yml'


def apply_animation(ui_element, num_of_beats, duration, relative_song_time):

	beat_duration = duration/num_of_beats
	beats_played = math.floor(relative_song_time / beat_duration)
	relative_beat_time = relative_song_time - beat_duration * beats_played
	percent_beat_time = relative_beat_time / beat_duration

	if beats_played % 2 == 0:
		color = Colors.hls_to_rgb(hue, 1 ,1)
	else:
		color = Colors.hls_to_rgb(hue + 0.1, 1 ,1)
	
	for i in range(len(ui_element.get_array())/3):
		ui_element.get_array()[i*3 : i*3+3] = color


# ui elements
flower = Flower()
sheep = SmallSheep()
grass = Grass()
sign = Sign()
lake = Lake()


with open(FILE, 'r') as f:
    song = yaml.load(f)

audio_file = "../Music/" + song['file_name']
pieces = song['pieces']
offset = song['offset']
current_piece_id = 0
print pieces[current_piece_id]

# init music
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer.music.load(audio_file)
pygame.mixer.music.play(0, 0)


frame_id = 0
hue = 0.3

while pygame.mixer.music.get_busy():
	song_time = (pygame.mixer.music.get_pos() / 1000.0) + offset

	if current_piece_id < len(pieces) -1 and song_time > pieces[current_piece_id+1][0]:
		current_piece_id += 1
		print pieces[current_piece_id]
		hue = 0.8 if hue == 0.3 else 0.3

	if current_piece_id == len(pieces) - 1:
		duration = 30.0
 	else:
 		duration = pieces[current_piece_id+1][0] - pieces[current_piece_id][0]


	num_of_beats = pieces[current_piece_id][1]
	relative_song_time = song_time - pieces[current_piece_id][0]

	apply_animation(flower, num_of_beats, duration, relative_song_time)
	apply_animation(sheep, num_of_beats, duration, relative_song_time)
	apply_animation(grass, num_of_beats, duration, relative_song_time)
	apply_animation(sign, num_of_beats, duration, relative_song_time)
	apply_animation(lake, num_of_beats, duration, relative_song_time)

	network.send(frame_id, flower.get_array(), sheep.get_array(), grass.get_array(), sign.get_array(), lake.get_array())

	clock.tick(50)
	frame_id += 1




