
class Lake:

	wave1 = range(1+1200, 53+1200)
	wave1_low_con = 77 - 179 + 534
	wave1_high_con = 126 - 179 + 534

	wave2 = range(55+1200, 131+1200)[::-1]
	wave2_low_con = 58 - 179 + 534
	wave2_high_con = 145 - 179 + 534

	wave3 = range(134+1200, 219+1200)
	wave3_low_con = 40 - 179 + 534
	wave3_high_con = 162 - 179 + 534

	wave4 = range(220+1200, 315+1200)[::-1]
	wave4_low_con = 22 - 179 + 534
	wave4_high_con = 180 - 179

	wave5 = range(317+1200, 423+1200)
	wave5_low_con = 4 - 179 + 534
	wave5_high_con = 203 - 179

	wave6 = range(426+1200, 522+1200)[::-1]
	wave6_low_con = 519 - 179
	wave6_high_con = 223 - 179

	wave7 = range(1+600, 92+600)
	wave7_low_con = 502 - 179
	wave7_high_con = 238 - 179

	wave8 = range(92+600, 183+600)[::-1]
	wave8_low_con = 487 - 179
	wave8_high_con = 255 - 179

	wave9 = range(184+600, 276+600)
	wave9_low_con = 472 - 179
	wave9_high_con = 268 - 179

	wave10 = range(279+600, 375+600)[::-1]
	wave10_low_con = 457 - 179
	wave10_high_con = 288 - 179

	wave11 = range(375+600, 464+600)
	wave11_low_con = 438 - 179
	wave11_high_con = 308 - 179

	wave12 = range(465+600, 528+600)[::-1]
	wave12_low_con = 422 - 179 
	wave12_high_con = 337 - 179

	wave13 = range(539+600, 584+600)
	wave13_low_con = 406 - 179 
	wave13_high_con = 353 - 179

	waves_arr = [wave1, wave2, wave3, wave4, wave5, wave6, wave7, wave8, wave9, wave10, wave11, wave12, wave13]
	conn_arr = [[wave1_low_con, wave1_high_con],
				[wave2_low_con, wave2_high_con],
				[wave3_low_con, wave3_high_con],
				[wave4_low_con, wave4_high_con],
				[wave5_low_con, wave5_high_con],
				[wave6_low_con, wave6_high_con],
				[wave7_low_con, wave7_high_con],
				[wave8_low_con, wave8_high_con],
				[wave9_low_con, wave9_high_con],
				[wave10_low_con, wave10_high_con],
				[wave11_low_con, wave11_high_con],
				[wave12_low_con, wave12_high_con],
				[wave13_low_con, wave13_high_con],
				]
	waves = wave1 + wave2 + wave3 + wave4 + wave5 + wave6 + wave7 + wave8 + wave9 + wave10 + wave11 + wave12 + wave13


	contour = range(0, 57) + range(58, 178) + range(178, 534)

	whole_lake = waves + contour 


	def __init__(self):
		self.clear()

	def clear(self):
		self.arr = [0, 0, 0] * 1800

	def get_all_indexes(self):
		return self.whole_lake

	def get_array(self):
		return self.arr

	def get_con_by_wave_id(self, wave_id):
		if wave_id < 1:
			return [ (self.wave1_high_con + self.wave1_low_con) / 2, (self.wave1_high_con + self.wave1_low_con) / 2]
		elif wave_id > 13:
			return [ (self.wave13_high_con + self.wave13_low_con) / 2, (self.wave13_high_con + self.wave13_low_con) / 2]
		else:
			return self.conn_arr[wave_id]






