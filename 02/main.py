file = open("data","r")
lines = file.readlines()
data = [line.replace("\n","") for line in lines]

#part 1
twice = 0
triple = 0
for line in data:
	c2=False
	c3=False
	dictionary = {letter:0 for letter in line}
	for letter in line:
		dictionary[letter]+=1	
	for number in dictionary.values():
		if number==2:
			c2=True
		elif number==3:
			c3=True
	if c2:
		twice+=1
	if c3:
		triple+=1
print twice*triple

#part 2
data2 = [[letter for letter in line] for line in data]

for line in data2:
	for l in data2:
		dif = 0
		for i in range(len(line)):
			if line[i]!=l[i]:
				dif+=1
		if dif==1:
			print line
			print l
