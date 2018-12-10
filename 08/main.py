file = open('data','r')
data = map(int,file.readline().split())

def fun(data):
	child = data[0]
	metadata = data[1]
	data = data[2:]
	for i in range(child):
		data = fun(data)
	for i in range(metadata):
		fun.s += data[i]
	data = data[metadata:]
	return data

fun.s = 0
data = fun(data)

print fun.s
