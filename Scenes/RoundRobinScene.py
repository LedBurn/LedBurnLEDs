from Scene import Scene

import sys, os
sys.path.append(os.path.abspath('../Animations_Flower'))
from RoundRobinFlowerAnimation import RoundRobinFlowerAnimation

sys.path.append(os.path.abspath('../Animations_Grass'))
from RoundRobinGrassAnimation import RoundRobinGrassAnimation

# sys.path.append(os.path.abspath('../Animations_Sheep'))
# from FireSheepAnimation import FireSheepAnimation

# sys.path.append(os.path.abspath('../Animations_Sign'))
# from FireSignAnimation import FireSignAnimation


class RoundRobinScene(Scene):
	def __init__(self, flower, sheep, grass, sign):
		Scene.__init__(self, flower, sheep, grass, sign)

		self.animations = [RoundRobinFlowerAnimation(flower),
							RoundRobinGrassAnimation(grass)]

	def apply(self, time_percent):
		for animation in self.animations:
			animation.apply(time_percent)
		