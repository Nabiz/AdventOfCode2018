from collections import OrderedDict
file = open('data','r')
data = [line.replace('Step ','').replace(' must be finished before step ','').replace(' can begin.\n','') for line in file]

notavalible = sorted(list({i[1] for i in data}))
avalible = sorted(list({i[0] for i in data if i[0] not in notavalible}))
steps = {d[1]:'' for d in data}
steps = OrderedDict(sorted(steps.items()))

for s in steps:
	for d in data:
		if d[1]==s:
			steps[s]+=d[0]

result = ''
while len(notavalible)>0:
	a=avalible[0]
	result+=a
	steps.pop(a, None)
	del avalible[0]
	for s in steps:
		for req in steps[s]:
			if req not in result:
				break
		else:
			if s not in avalible:
				avalible.append(s)
	
	for a in avalible:
		if a in notavalible:
			notavalible.remove(a)
	
	avalible.sort()

	print 'wynik', result
	