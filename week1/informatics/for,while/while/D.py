n = int(input())

while(n>=1):
	if(n==1):
		print("YES")
		break
	else:
		if(n%2==0):
			if(n/2==1):
				print("YES")
				break
			else:
				n = n/2
		else:
			print("NO")
			break