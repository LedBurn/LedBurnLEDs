

# pieces = [[0,44],
# [18.92426304,	32], 
# [25.77414966,	16],
# [39.49714286,	16],
# [53.1969161,	44],
# [72.05151927,	32],
# [78.92462585,	16],
# [92.62439909,	16],
# [106.3473923,	44],
# [125.2019955,	32],
# [132.075102	,	16],
# [145.7748753,	16],
# [159.4746483	,0]]

# pieces = [[0,	64],
# [28.49088435,	32],
# [42.51573696,	32],
# [56.54058957,	64],
# [84.56707483,	64],
# [112.5935601,	96],
# [154.621678,	64],
# [182.6713832,	64],
# [210.6746485,	64],
# [238.7243537,	32],
# [252.7259864,	64],
# [280.7524717,	64],
# [308.8021769,	64],
# [336.8286621,	24],
# [347.3240816,	8],
# [350.8302948,	80],
# [385.8692063,	64],
# [413.8956914,	64],
# [441.9221765,	0]]




import sys, os
sys.path.append(os.path.abspath('../Network'))
import LedBurnProtocol as network
import time
import math
import pygame
import yaml

sys.path.append(os.path.abspath('../UIElements'))
from Flower import Flower
from SmallSheep import SmallSheep
from Grass import Grass
from Sign import Sign

sys.path.append(os.path.abspath('../Animations_Flower'))
from FlowerAnimationFactory import FlowerAnimationFactory


flower_animation = None
flower_animation_mul = 1

def create_animations(animation_dict):
	if 'flower' in animation_dict: 
		global flower_animation, flower_animation_mul
		flower_animation = FlowerAnimationFactory.create_animation(animation_dict['flower'], flower)
		if 'beat_mul' in animation_dict['flower']:
			flower_animation_mul = animation_dict['flower']['beat_mul']
		else:
			flower_animation_mul = 1
	else:
		flower_animation = None

def apply_animation(animation, num_of_beats, duration, relative_song_time):
	if (animation == None):
		return

	beat_duration = duration/num_of_beats
	beats_played = math.floor(relative_song_time / beat_duration)
	relative_beat_time = relative_song_time - beat_duration * beats_played
	percent_beat_time = relative_beat_time / beat_duration

	animation.apply(percent_beat_time)


# ui elements
flower = Flower()
sheep = SmallSheep()
grass = Grass()
sign = Sign()


# open file
# FILE = 'Teletubbies.yml'
# FILE = 'Dreamfunk.yml'
FILE = 'Soul Orchestra.yml'

with open(FILE, 'r') as f:
    song = yaml.load(f)

audio_file = "../Music/" + song['file_name']
pieces = song['pieces']
current_piece_id = 0

# init music
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer.music.load(audio_file)
pygame.mixer.music.play(0, 0)


create_animations(pieces[current_piece_id][2])
frame_id = 0

while pygame.mixer.music.get_busy():
	song_time = (pygame.mixer.music.get_pos() - 170)/ 1000.0

	if current_piece_id < len(pieces) -1 and song_time > pieces[current_piece_id+1][0]:
		current_piece_id += 1
		create_animations(pieces[current_piece_id][2])

	if current_piece_id == len(pieces) - 1:
		duration = 30.0
 	else:
 		duration = pieces[current_piece_id+1][0] - pieces[current_piece_id][0]


	num_of_beats = pieces[current_piece_id][1]
	relative_song_time = song_time - pieces[current_piece_id][0]

	#flower
	flower_num_of_beats = num_of_beats* flower_animation_mul
	apply_animation(flower_animation, flower_num_of_beats, duration, relative_song_time)


	network.send(frame_id, flower.get_array(), sheep.get_array(), grass.get_array(), sign.get_array())

	clock.tick(50)
	frame_id += 1




