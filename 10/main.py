from __future__ import print_function
#file = open('example','r')
file = open('data','r')
data = [map(int,line.replace('position=<','').replace('>',',').replace('velocity=<','').replace(',\n','').split(',')) for line in file]
position = [[d[0],d[1]] for d in data]
velocity = [[d[2],d[3]] for d in data]
'''
for i in range(5):
	for x in range(-100,100):
		for y in range(-100,100):
			if [y,x] in position:
				print('#',end='')
			else:
				print(' ',end='')
		print('')
	print('===================')
	for j in range(len(position)):
		position[j][0]+=velocity[j][0]
		position[j][1]+=velocity[j][1]
'''

for i in range(10600):
	#t = True
	for j in range(len(position)):
		position[j][0]+=velocity[j][0]
		position[j][1]+=velocity[j][1]
	#for j in range(len(position)):
		#if abs(position[j][0]-position[j][1])>100:
			#t=False
	#if t:
	if i in range(10515,10525):
		#print(position)
		for x in range(50,200):
			for y in range(50,200):
				if [y,x] in position:
					print('#',end='')
				else:
					print('.',end='')
			print('')
		print(i, '<==========================')


