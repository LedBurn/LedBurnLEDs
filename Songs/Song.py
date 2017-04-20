import math

import Network.LedBurnProtocol as network
import pygame
import yaml

from UIElements.Flower import Flower
from UIElements.SmallSheep import SmallSheep
from UIElements.Grass import Grass
from UIElements.Sign import Sign
from UIElements.Lake import Lake

from Animations_Flower.FlowerAnimationFactory import FlowerAnimationFactory
from Animations_Grass.GrassAnimationFactory import GrassAnimationFactory
from Animations_Lake.LakeAnimationFactory import LakeAnimationFactory

class Song():
	def __init__(self, file_name):
		self.file_name = file_name

		self.flower_animation = None
		self.flower_animation_mul = 1
		self.grass_animation = None
		self.grass_animation_mul = 1
		self.lake_animation = None
		self.lake_animation_mul = 1

		self.flower = Flower()
		self.sheep = SmallSheep()
		self.grass = Grass()
		self.sign = Sign()
		self.lake = Lake()

		with open(self.file_name, 'r') as f:
			self.song_yml = yaml.load(f)
		self.audio_file = "Music/" + self.song_yml['file_name']
		self.pieces = self.song_yml['pieces']
		self.current_piece_id = 0

		self.create_animations(self.pieces[self.current_piece_id][2])
		self.frame_id = 0

	def get_audio_file(self):
		return self.audio_file

	def create_animations(self, animation_dict):
		if 'flower' in animation_dict: 
			self.flower_animation = FlowerAnimationFactory.create_animation(animation_dict['flower'], self.flower)
			if 'beat_mul' in animation_dict['flower']:
				self.flower_animation_mul = animation_dict['flower']['beat_mul']
			else:
				self.flower_animation_mul = 1
		else:
			self.flower_animation = None

		if 'grass' in animation_dict:
			self.grass_animation = GrassAnimationFactory.create_animation(animation_dict['grass'],self.grass)
			if 'beat_mul' in animation_dict['grass']:
				self.grass_animation_mul = animation_dict['grass']['beat_mul']
			else:
				self.grass_animation_mul = 1
		else:
			self.grass_animation = None

		if 'lake' in animation_dict:
			self.lake_animation = LakeAnimationFactory.create_animation(animation_dict['lake'], self.lake)
			if 'beat_mul' in animation_dict['lake']:
				self.lake_animation_mul = animation_dict['lake']['beat_mul']
			else:
				self.lake_animation_mul = 1
		else:
			self.lake_animation = None


	def apply_animation(self, animation, num_of_beats, duration, relative_song_time):
		if (animation == None):
			return

		beat_duration = duration/num_of_beats
		beats_played = math.floor(relative_song_time / beat_duration)
		relative_beat_time = relative_song_time - beat_duration * beats_played
		percent_beat_time = relative_beat_time / beat_duration

		animation.apply(percent_beat_time)


	def play_animations(self, song_time):

		if self.current_piece_id < len(self.pieces) -1 and song_time > self.pieces[self.current_piece_id+1][0]:
			self.current_piece_id += 1
			self.create_animations(self.pieces[self.current_piece_id][2])

		if self.current_piece_id == len(self.pieces) - 1:
			duration = 30.0
	 	else:
	 		duration = self.pieces[self.current_piece_id+1][0] - self.pieces[self.current_piece_id][0]

		num_of_beats = self.pieces[self.current_piece_id][1]
		relative_song_time = song_time - self.pieces[self.current_piece_id][0]

		if (self.flower_animation != None):
			flower_num_of_beats = num_of_beats * self.flower_animation_mul
			self.apply_animation(self.flower_animation, flower_num_of_beats, duration, relative_song_time)

		if (self.grass_animation != None):
			grass_num_of_beats = num_of_beats * self.grass_animation_mul
			self.apply_animation(self.grass_animation, grass_num_of_beats, duration, relative_song_time)

		if (self.lake_animation != None):
			lake_num_of_beats = num_of_beats *  self.lake_animation_mul
			self.apply_animation(self.lake_animation, lake_num_of_beats, duration, relative_song_time)

		network.send(self.frame_id, 
			self.flower.get_array(), 
			self.sheep.get_array(), 
			self.grass.get_array(), 
			self.sign.get_array(),
			 self.lake.get_array())

		self.frame_id += 1


