from math import*
n = int(input())
i = 1
while(i<=n):
	if(i%(sqrt(i))==0):
		print(i)
	i+=1