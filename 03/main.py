file = open("data","r")
data = [line.replace("@","").split() for line in file]
data = [[int(line[0].replace("#",'')),map(int,(line[1].replace(':','').split(","))),map(int,line[2].split('x'))] for line in data]
n = 1000

#part1
square = [[[] for i in range(n)] for j in range(n)]
for i in data:
	for x in range(i[2][0]):
		for y in range(i[2][1]):
			square[i[1][0]+x][i[1][1]+y].append(i[0])

count = 0
for x in range(n):
	for y in range(n):
		if len(square[x][y]) > 1:
			count+=1
print count

#part2
for i in data:
	t = True
	for x in range(i[2][0]):
		for y in range(i[2][1]):
			if len(square[i[1][0]+x][i[1][1]+y])  > 1:
				t = False
	if t:
		print i[0]
		break


