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