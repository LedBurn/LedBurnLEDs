class Scene(object):
	def __init__(self, flower, sheep, grass, sign):
		super(Scene, self).__init__()
		self.flower = flower
		self.sheep = sheep
		self.grass = grass
		self.sign = sign


	def apply(self, time_percent):
		pass