import random
import sys
import os
import time

sys.path.append(os.path.abspath('../Network'))
import LedBurnProtocol as network

frame = 0
while True:

	r = 255
	g = 80
	b = 40

	arr = [10, 10 ,10] * 150
	for x in range(150):
		flicker = random.randrange(0, 80)
		r1 = r-flicker
		g1 = g-flicker
		b1 = b-flicker
		
		if(g1<0): g1=0
		if(r1<0): r1=0
		if(b1<0): b1=0

		arr[x * 3 : x * 3 + 3] = [r1, g1, b1]

	print len(arr)

	flower = [200, 0, 0] * 550
	sheep = [200, 0 ,0] * 302
	grass = [0, 200, 0] * 600
	#sign = [0, 0, 200] * 150
	network.send(flower, sheep, grass, arr)
	time.sleep(0.1)
	frame += 1