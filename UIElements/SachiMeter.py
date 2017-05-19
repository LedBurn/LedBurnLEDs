
class SachiMeter:

	sachi_color 	= [128, 0, 128]
	stoned_color 	= [0, 255 , 0]
	zero_color 		= [0, 96, 159]
	clear 			= [0, 0, 0]

	def __init__(self):
		self.arr = [0,0,0] * 7

	def get_array(self):
		return self.arr

	def set_sachi_meter(self, val):
		if val == -3:
			self.arr = 	self.sachi_color*3 + 				self.zero_color + 		self.clear*3
		elif val == -2:
			self.arr = 	self.clear+self.sachi_color*2 + 	self.zero_color + 		self.clear*3
		elif val == -1:
			self.arr = 	self.clear*2+self.sachi_color + 	self.zero_color + 		self.clear*3
		elif val == 0:
			self.arr = 	self.clear*3 + 						self.zero_color + 		self.clear*3
		elif val == 1:
			self.arr = 	self.clear*3 + 						self.zero_color + 		self.stoned_color+self.clear*2
		elif val == 2:
			self.arr = 	self.clear*3 + 						self.zero_color + 		self.stoned_color*2+self.clear*1
		elif val == 3:
			self.arr = 	self.clear*3 + 						self.zero_color + 		self.stoned_color*3


