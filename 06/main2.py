file = open("data","r")
points = [map(int,line.split(", ")) for line in file]

xmax =  max(points)[0]
ymax = max(points, key=lambda x:x[1])[1]

count = 0
for i in range(xmax+1):
	for j in range(ymax+1):
		s = 0
		for p in points:
			s+=abs(p[0]-i)+abs(p[1]-j)
			if s>10000:
				break
		else:
			count+=1
print count
