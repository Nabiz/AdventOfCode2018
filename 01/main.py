file = open('data','r')
data = file.read()

#part1

print(eval(data.replace("\n", "")))

#part2

string = data.split()
freq = {0}

s = 0
b=False
while(True):
	for number in string:
		s += eval(number)
		if s in freq:
			print s
			b = True
			break
		freq.add(s)
	if b:
		break