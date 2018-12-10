file = open("data","r")
data = str(file.readlines()[0])[:-1]
data = [ord(l) for l in data]

def polymer(data):
	i = 0
	while i<len(data)-1:
		capital = 1 if 65<=data[i]<=90 else -1
		if capital*32+data[i] == data[i+1]:
			del data[i]
			del data[i]
			i-=1
		else:
			i+=1
	return len(data)
result = polymer(data)
print result

for i in range(65,91):
	data2 = [x for x in data if x!=i and x!=i+32]
	r = polymer(data2)
	if r < result:
		result = r 
print result