n = int(input())

i=1
k=1
while(i<=n):
	k = i
	while(k>=1):
		if(k==1):
			print(i,end=' ')
			break

		elif(k%2==0):
			if(k/2==1):
				print(i, end=' ')
				break
			else:
				k = k/2

		else:
			break	
	i+=1		

	