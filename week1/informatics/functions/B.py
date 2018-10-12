a = int(input())
n = int(input())
p = a
def  power(a,n):
	for i in range(n-1):
		 a = a*p

	return a

print(power(a,n))