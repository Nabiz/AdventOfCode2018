serial = 2568

grid = [[ 0 for i in range(301)] for j in range(301)]


for i in range(1,301):
	for j in range(1,301):
		rack = i+10
		val = (rack*j+serial)*rack
		grid[i][j] = int(str(val)[-3])-5


maximum = -5*9

for i in range(1,299):
	for j in range(1,299):
		power=0
		for i2 in range(i,i+3):
			for j2 in range(j,j+3):
				power += grid[i2][j2]
		if power>maximum:
			maximum=power
			x = i
			y = j

print maximum
print x,y

#part2
from math import sqrt
maximum = -5*300*300
notfind = 0
for s in range(0,int(sqrt(300))+1):
	for i in range(1,301-s+1):
		for j in range(1,301-s+1):
			power=0
			for i2 in range(i,i+s):
				for j2 in range(j,j+s):
					power += grid[i2][j2]
			if power>maximum:
				maximum=power
				x = i
				y = j
				size = s

print maximum
print x,y,size