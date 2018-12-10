players = 427
last = 70723 * 100
#players = 21
#last = 6111

circle = [0]
score = [0 for p in range(players)]
i=0
player=0
for m in range(1,last+1):
	player=(player+1) % players
	i+=2
	if i>len(circle):
		i-=len(circle)
	if m%23==0:
		i-=9
		if i<0:
			i+=len(circle)
		score[player]+=circle[i]+m
		del circle[i]
	else:
			circle.insert(i,m)

print circle

maximmum = max(score)
print maximmum