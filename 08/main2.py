def fun():
	node = Node(fun.data)
	fun.data = fun.data[2:]
	for i in range(node.childNum):
		node.childs.append(fun())
	for i in range(node.metaLen):
		node.meta.append(fun.data[i])
	fun.data = fun.data[node.metaLen:]
	return node

file = open('data','r')
fun.data = map(int,file.readline().split())

class Node():
	def __init__(self, data):
		self.childNum = data[0]
		self.metaLen = data[1]
		self.childs = []
		self.meta = []
		self.value = 0
	def val(self):
		if self.childNum == 0:
			self.value=sum(self.meta)
		else:
			value = 0
			for m in self.meta:
				if m<=self.childNum:
					value+= self.childs[m-1].val()
			self.value = value
		return self.value
		
root = fun()
root.val()
print root.value
