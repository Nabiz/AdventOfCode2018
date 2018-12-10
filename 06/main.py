from copy import *
file = open("data","r")
points = [map(int,line.split(", ")) for line in file]

xmax =  max(points)[0]
ymax = max(points, key=lambda x:x[1])[1]
xd = len(points)

grid = [[0 for i in range(ymax+1)] for j in range(xmax+1)]
it = [[0 for i in range(ymax+1)] for j in range(xmax+1)]

count = 1
for i in range(xmax+1):
	for j in range(ymax+1):
		for p in points:
			if i==p[0] and j==p[1]:
				grid[i][j]=count
				count+=1

i=1
while len(points)>0:
	last=points[-1]
	newpoints=[]
	for p in points:
		x=p[0]
		y=p[1]
		v=grid[x][y]
		if 0<x:
			if grid[x-1][y]==0:
				grid[x-1][y]=v
				newpoints.append([x-1,y])
				it[x-1][y]=i
			elif grid[x-1][y]!=v and grid[x-1][y]!=-1 and i==it[x-1][y]:
				grid[x-1][y]=-1
				
		if x<xmax:
			if grid[x+1][y]==0:
				grid[x+1][y]=v
				newpoints.append([x+1,y])
				it[x+1][y]=i
			elif grid[x+1][y]!=v and grid[x+1][y]!=-1 and i==it[x+1][y]:
				grid[x+1][y]=-1
		
		if 0<y:
			if grid[x][y-1]==0:
				grid[x][y-1]=v
				newpoints.append([x,y-1])
				it[x][y-1]=i
			elif grid[x][y-1]!=v and grid[x][y-1]!=-1 and i==it[x][y-1]:
				grid[x][y-1]=-1
		
		if y<ymax:
			if grid[x][y+1]==0:
				grid[x][y+1]=v
				newpoints.append([x,y+1])
				it[x][y+1]=i
			elif grid[x][y+1]!=v and grid[x][y+1]!=-1 and i==it[x][y+1]:
				grid[x][y+1]=-1

		if p==last:
			i+=1
			points=deepcopy(newpoints)

expect = set()
for i in range(xmax+1):
	expect.add(grid[i][0])
	expect.add(grid[i][ymax])

for i in range(ymax+1):
	expect.add(grid[0][i])
	expect.add(grid[xmax][i])

maximum = 0
for n in range(xd):
	c=0
	for i in range(xmax+1):
		for j in range(ymax+1):
			if n==grid[i][j]:
				c+=1
	print c
	if c > maximum and n not in expect:
		maximum = c

print maximum
