file=open("data","r")
data = [line.split(']') for line in file]
for line in data:
	line[0]=map(int,line[0].replace('[','').replace('-','').replace(':','').split())
	if line[1]==' wakes up\n':
		line[1]=line[1].replace(' wakes up\n','w')
	elif line[1]==' falls asleep\n':
		line[1]=line[1].replace(' falls asleep\n','f')
	else:
		line[1]=int(line[1].replace('Guard #','').replace(' begins shift\n',''))

data = sorted(data, key=lambda x: (x[0][0],x[0][1]))

sleep = {}
for line in data:
	if isinstance(line[1],int):
		guard=line[1]
		if guard not in sleep:
			sleep[guard] = [0 for i in range(60)]
	elif line[1]=='f':
		fall = line[0][1]
	else:
		wake = line[0][1]
		for i in range(fall,wake):
			sleep[guard][i]+=1

maximum = -1
for i in sleep:
	if sum(sleep[i]) > maximum:
		maximum=sum(sleep[i])
		guard=i
		minute = sleep[i].index(max(sleep[i]))
print guard*minute

#part2
maximum = -1
for i in sleep:
	for j in sleep[i]:
		if j>maximum:
			maximum=j
			guard=i
			minute=sleep[i].index(j)
print guard*minute
