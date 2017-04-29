import math

import Network.LedBurnProtocol as network
import pygame
import yaml

from UIElements.Flower import Flower
from UIElements.SmallSheep import SmallSheep
from UIElements.Grass import Grass
from UIElements.Sign import Sign
from UIElements.Lake import Lake
from UIElements.TempStick import TempStick

from Animations_Flower.FlowerAnimationFactory import FlowerAnimationFactory
from Animations_Grass.GrassAnimationFactory import GrassAnimationFactory
from Animations_Lake.LakeAnimationFactory import LakeAnimationFactory
from Animations_Sheep.SheepAnimationFactory import SheepAnimationFactory
from Animations_Sign.SignAnimationFactory import SignAnimationFactory

class Song():
	def __init__(self, file_name):
		self.file_name = file_name

		self.flower_animation = None
		self.flower_animation_mul = 1
		self.grass_animation = None
		self.grass_animation_mul = 1
		self.lake_animation = None
		self.lake_animation_mul = 1
		self.sheep_animation = None
		self.sheep_animation_mul = 1
		self.sign_animation = None
		self.sign_animation_mul = 1

		self.flower = Flower()
		self.sheep = SmallSheep()
		self.grass = Grass()
		self.sign = Sign()
		self.lake = Lake()
		self.temp_stick = TempStick()

		with open(self.file_name, 'r') as f:
			self.song_yml = yaml.load(f)
		self.audio_file = "Music/" + self.song_yml['file_name']
		self.pieces = self.song_yml['pieces']
		self.current_piece_id = 0
		self.offset = self.song_yml['offset']

		print str(self.pieces[self.current_piece_id][0]) + " - " + str(self.pieces[self.current_piece_id][1])
		self.create_animations(self.pieces[self.current_piece_id][2])
		self.frame_id = 0

	def get_audio_file(self):
		return self.audio_file


	def get_effect(self, animation_dict, name, element, factory):
		if animation_dict != None and name in animation_dict: 
			if 'Clear' in animation_dict[name]:
				element.clear()
				return None
			else:	
				return factory.create_animation(animation_dict[name], element)
		else:
			return None

	def get_mul(self, animation_dict, name):
		if animation_dict != None and name in animation_dict and 'beat_mul' in animation_dict[name]:
			return animation_dict[name]['beat_mul']
		return 1.0

	def create_animations(self, animation_dict):
	
		self.flower_animation = self.get_effect(animation_dict, 'flower', self.flower, FlowerAnimationFactory)
		self.flower_animation_mul = self.get_mul(animation_dict, 'flower')

		self.grass_animation = self.get_effect(animation_dict, 'grass', self.grass, GrassAnimationFactory)
		self.grass_animation_mul = self.get_mul(animation_dict, 'grass')

		self.lake_animation = self.get_effect(animation_dict, 'lake', self.lake, LakeAnimationFactory)
		self.lake_animation_mul = self.get_mul(animation_dict, 'lake')

		self.sheep_animation = self.get_effect(animation_dict, 'sheep', self.sheep, SheepAnimationFactory)
		self.sheep_animation_mul = self.get_mul(animation_dict, 'sheep')

		self.sign_animation = self.get_effect(animation_dict, 'sign', self.sign, SignAnimationFactory)
		self.sign_animation_mul = self.get_mul(animation_dict, 'sign')


	def apply_animation(self, animation, num_of_beats, duration, relative_song_time):
		if (animation == None):
			return

		beat_duration = duration/num_of_beats
		beats_played = math.floor(relative_song_time / beat_duration)
		relative_beat_time = relative_song_time - beat_duration * beats_played
		percent_beat_time = relative_beat_time / beat_duration

		animation.apply(percent_beat_time)

	def clear_leds(self):
		self.flower.clear()
		self.sheep.clear()
		self.grass.clear()
		self.sign.clear()
		self.lake.clear()

	def play_animations(self, song_time, curr_temerature):

		song_time += self.offset

		self.temp_stick.set_temperature(curr_temerature)

		if self.current_piece_id < len(self.pieces) -1 and song_time > self.pieces[self.current_piece_id+1][0]:
			self.current_piece_id += 1
			print str(self.pieces[self.current_piece_id][0]) + " - " + str(self.pieces[self.current_piece_id][1])
			self.create_animations(self.pieces[self.current_piece_id][2])

		if self.current_piece_id == len(self.pieces) - 1:
			duration = 30.0
	 	else:
	 		duration = self.pieces[self.current_piece_id+1][0] - self.pieces[self.current_piece_id][0]

		num_of_beats = self.pieces[self.current_piece_id][1]
		relative_song_time = song_time - self.pieces[self.current_piece_id][0]

		if self.flower_animation != None:
			flower_num_of_beats = num_of_beats * self.flower_animation_mul
			self.apply_animation(self.flower_animation, flower_num_of_beats, duration, relative_song_time)

		if self.grass_animation != None:
			grass_num_of_beats = num_of_beats * self.grass_animation_mul
			self.apply_animation(self.grass_animation, grass_num_of_beats, duration, relative_song_time)

		if self.lake_animation != None:
			lake_num_of_beats = num_of_beats *  self.lake_animation_mul
			self.apply_animation(self.lake_animation, lake_num_of_beats, duration, relative_song_time)

		if self.sheep_animation != None:
			sheep_num_of_beats = num_of_beats * self.sheep_animation_mul
			self.apply_animation(self.sheep_animation, sheep_num_of_beats, duration, relative_song_time)

		if self.sign_animation != None:
			sign_num_of_beats = num_of_beats * self.sign_animation_mul
			self.apply_animation(self.sign_animation, sign_num_of_beats, duration, relative_song_time)

		network.send(self.frame_id, 
			self.flower.get_array(), 
			self.sheep.get_array(), 
			self.grass.get_array(), 
			self.sign.get_array(),
			self.lake.get_array(),
			self.temp_stick.get_array())

		self.frame_id += 1


