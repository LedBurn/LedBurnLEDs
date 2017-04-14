import pygame
import random

#Fire Logic

# yellow
# orange
# red

current_state = [];


level = 3;


PIXEL_SIZE = 12
SIZE = [PIXEL_SIZE * 200, PIXEL_SIZE * 100]
FLOWER_MAPPING = [(46, 33), (46, 34), (46, 35), (46, 36), (45, 36), (45, 37), (45, 38), (44, 38), (44, 39), (44, 40), (43, 40), (43, 41), (43, 42), (42, 42), (41, 42), (40, 42), (40, 41), (39, 41), (39, 40), (39, 39), (40, 39), (40, 38), (40, 37), (41, 37), (42, 36), (42, 35), (43, 34), (43, 33), (44, 33), (38, 0), (44, 32), (43, 32), (42, 33), (41, 34), (40, 34), (39, 35), (38, 35), (38, 36), (37, 36), (36, 37), (35, 38), (34, 38), (33, 38), (32, 37), (32, 36), (32, 35), (32, 34), (33, 34), (34, 34), (34, 33), (35, 33), (35, 32), (36, 32), (37, 32), (37, 31), (38, 31), (39, 31), (40, 31), (41, 31), (39, 0), (41, 29), (40, 29), (39, 29), (38, 29), (37, 29), (36, 29), (35, 30), (34, 30), (33, 30), (32, 30), (31, 30), (30, 30), (30, 29), (30, 28), (30, 27), (30, 26), (31, 26), (32, 26), (32, 25), (33, 25), (34, 25), (35, 25), (36, 25), (37, 25), (38, 25), (39, 25), (39, 26), (40, 26), (41, 26), (40, 0), (41, 24), (40, 24), (39, 23), (38, 23), (37, 23), (36, 23), (35, 23), (34, 22), (33, 22), (32, 22), (31, 22), (30, 21), (30, 20), (30, 19), (31, 18), (32, 18), (33, 18), (34, 18), (35, 18), (35, 19), (36, 19), (37, 19), (38, 19), (38, 20), (39, 20), (40, 20), (40, 21), (41, 21), (41, 0), (43, 21), (43, 20), (43, 19), (42, 18), (42, 17), (41, 17), (40, 16), (39, 15), (39, 14), (38, 13), (37, 12), (38, 11), (39, 10), (40, 9), (41, 9), (42, 9), (43, 9), (43, 10), (43, 11), (44, 11), (44, 12), (44, 13), (44, 14), (45, 14), (45, 15), (45, 16), (45, 17), (46, 17), (46, 18), (46, 19), (42, 0), (49, 19), (49, 18), (49, 17), (49, 16), (49, 15), (50, 14), (50, 13), (50, 12), (50, 11), (50, 10), (50, 9), (51, 8), (52, 8), (53, 8), (54, 9), (54, 10), (54, 11), (54, 12), (54, 13), (55, 14), (55, 15), (55, 16), (55, 17), (54, 17), (54, 18), (54, 19), (53, 19), (52, 19), (43, 0), (54, 21), (55, 20), (56, 19), (57, 18), (58, 17), (59, 16), (60, 15), (61, 15), (62, 16), (63, 17), (64, 18), (64, 19), (64, 20), (64, 21), (63, 22), (62, 22), (62, 23), (61, 23), (60, 23), (60, 24), (60, 25), (59, 25), (58, 25), (58, 26), (58, 27), (57, 27), (57, 28), (56, 28), (55, 28), (44, 0), (55, 29), (56, 29), (57, 29), (58, 29), (59, 29), (60, 29), (60, 28), (61, 28), (62, 28), (63, 28), (64, 28), (65, 28), (66, 28), (67, 28), (67, 29), (67, 30), (67, 31), (66, 31), (65, 31), (64, 31), (63, 31), (62, 31), (61, 31), (60, 31), (59, 31), (59, 32), (58, 32), (57, 32), (56, 32), (45, 0), (55, 33), (56, 33), (57, 34), (58, 34), (59, 34), (60, 34), (61, 34), (61, 35), (62, 35), (63, 35), (63, 36), (64, 36), (65, 36), (66, 36), (66, 37), (65, 38), (65, 39), (64, 40), (63, 40), (62, 40), (61, 39), (60, 39), (59, 39), (58, 38), (57, 38), (56, 38), (56, 37), (55, 37), (55, 36), (54, 35), (46, 0), (47, 0), (52, 35), (52, 36), (52, 37), (53, 38), (53, 39), (53, 40), (53, 41), (53, 42), (53, 43), (53, 44), (52, 45), (51, 45), (50, 45), (49, 45), (48, 45), (47, 44), (47, 43), (47, 42), (47, 41), (46, 41), (46, 40), (46, 39), (47, 39), (47, 38), (48, 38), (48, 37), (48, 36), (48, 35), (49, 0), (50, 0), (47, 24), (49, 25), (49, 29), (44, 29), (43, 24), (48, 21), (53, 23), (53, 26), (53, 31), (52, 33), (48, 33), (51, 21), (46, 22), (46, 27), (51, 28), (51, 23), (47, 31), (43, 26), (53, 29), (51, 32), (48, 27), (54, 25), (51, 25), (45, 22), (44, 31), (47, 29), (43, 28), (45, 25), (44, 22), (49, 23), (50, 27), (50, 30), (48, 32), (45, 27), (53, 24), (47, 26), (47, 20), (54, 27), (46, 23), (50, 33), (52, 27), (46, 31), (45, 28), (50, 21), (53, 21), (54, 32), (48, 30), (51, 30), (44, 24)]
FLOWER_OFFSET = (0, 0)

pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
done = False

#YELLOW = hsl(60, 100%, 50%)
#rgc(255,255,0)
#rgb(139,0,0)

#30
#67



# min_x = 200;
# max_x = 0
# for i in range(len(FLOWER_MAPPING)):
# 	if FLOWER_MAPPING[i][0]<min_x:
# 		min_x = FLOWER_MAPPING[i][0]
# 		print(FLOWER_MAPPING[i])
# 		print(i)

# 	if FLOWER_MAPPING[i][0]>max_x:
# 		max_x = FLOWER_MAPPING[i][0]

# print min_x
# print max_x

def randomStart() :
	return [random.randrange(210, 255), random.randrange(180, 255) , 10]

def levelUp(fire, level, decrease) :
	for i in range(37):
		original = fire[i][level+1]

		if (original[0] <= 50):
			r = int (10 + (original[0]-10)*decrease) 
			g = original[1]
			b = original[2]

		else:
			r = int (50 + (original[0]-50)*decrease)
			g = int (10 + (original[1]-10)*decrease*0.9)
			b = original[2]

		new = [r, g ,b]
		print new
		fire[i][level] = new
		print i
		print level


FIRST_LEVEL_INDEXES = [281, 282, 283, 284, 285]


def animatePoint(fromColor, toColor, percent):
	r = animateInt(fromColor[0], toColor[0], percent)
	g = animateInt(fromColor[1], toColor[1], percent)
	b = animateInt(fromColor[2], toColor[2], percent)
	return [r, g, b]

def animateInt(fromInt, toInt, percent):
	if (fromInt > toInt):
		diff = fromInt - toInt
		return fromInt - diff*percent
	else:
		diff = toInt - fromInt
		return fromInt + diff*percent


def animateToFrame(fromFrame, toFrame):
	frameCounter = 0.0
	while frameCounter < 2:
		newArr = [[animatePoint(fromFrame[j][i], toFrame[j][i], frameCounter/2.0) for i in range(46)] for j in range(38)]

		frameCounter += 1.0
	 	
	 	for index in range(len(FLOWER_MAPPING)):
 			color = newArr[FLOWER_MAPPING[index][0]-30][FLOWER_MAPPING[index][1]]
			rect = [PIXEL_SIZE * (FLOWER_MAPPING[index][0] + FLOWER_OFFSET[0]), PIXEL_SIZE * (FLOWER_MAPPING[index][1] + FLOWER_OFFSET[1]), PIXEL_SIZE, PIXEL_SIZE]
			pygame.draw.rect(screen, color, rect, 0)

		pygame.display.flip()

		clock.tick(50)
		for event in pygame.event.get():  # user did something
			if event.type == pygame.QUIT:
				done = True


counter = 0
newFire = [[[10, 10, 10] for i in range(46)] for j in range(38)]
while not done:
	counter += 1
	flower = [20,20,20] * len(FLOWER_MAPPING)

	oldFire = newFire;
	newFire = [[[10, 10, 10] for i in range(46)] for j in range(38)]

	for i in range(37):
		newFire[i][45] = randomStart()

	for i in range(44, 0, -1):
		if (i > 30):
			levelUp(newFire, i, 0.999)
		else:
			levelUp(newFire, i, 0.999)

	animateToFrame(oldFire, newFire)
	# levelUp(44, 0.7)
	# levelUp(43, 0.7)
	# levelUp(42, 0.7)


 # 	for index in range(len(FLOWER_MAPPING)):
 # 		color = fire[FLOWER_MAPPING[index][0]-30][FLOWER_MAPPING[index][1]]
	# 	rect = [PIXEL_SIZE * (FLOWER_MAPPING[index][0] + FLOWER_OFFSET[0]), PIXEL_SIZE * (FLOWER_MAPPING[index][1] + FLOWER_OFFSET[1]), PIXEL_SIZE, PIXEL_SIZE]
	# 	pygame.draw.rect(screen, color, rect, 0)

	# pygame.display.flip()

	# clock.tick(3)
	# for event in pygame.event.get():  # user did something
	# 	if event.type == pygame.QUIT:
	# 		done = True

import pygame








