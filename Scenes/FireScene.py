from Scene import Scene

import sys, os
sys.path.append(os.path.abspath('../Animations_Grass'))
from FireGrassAnimation import FireGrassAnimation

sys.path.append(os.path.abspath('../Animations_Sheep'))
from FireSheepAnimation import FireSheepAnimation

sys.path.append(os.path.abspath('../Animations_Sign'))
from FireSignAnimation import FireSignAnimation


class FireScene(Scene):
	def __init__(self, flower, sheep, grass, sign):
		Scene.__init__(self, flower, sheep, grass, sign)

		self.animations = [FireSheepAnimation(sheep),
							FireGrassAnimation(grass),
							FireSignAnimation(sign)]

	def apply(self, time_percent):
		for animation in self.animations:
			animation.apply(time_percent)
		