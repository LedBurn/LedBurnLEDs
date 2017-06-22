
class SachiMeter:

	sachi_color 	= [128, 0, 128]
	stoned_color 	= [0, 255 , 0]
	zero_color 		= [0, 96, 159]
	clear 			= [0, 0, 0]

	def __init__(self):
		self.arr = [0,0,0] * 7
		self.is_input_mode = False

	def get_array(self):
		return self.arr

	def set_sachi_meter(self, time_percent, val):
		if val is None:
			self.arr = [0,0,0] * 7

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

		brightness = 1.0
		if self.is_input_mode and time_percent is not None:
			time_percent = (time_percent % 0.2) * 5.0
			brightness = time_percent * 2.0 if time_percent < 0.5 else 2.0 - time_percent * 2.0
		for i in range(0, len(self.arr)):
			self.arr[i] = int(self.arr[i] * brightness)


	def set_is_input_mode(self, val):
		if self.is_input_mode == val:
			return
		self.is_input_mode = val



