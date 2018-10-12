n = int(input())
arr = []
count = 0
for i in range(n):
	arr.append(int(input()))


for i in range(1,n-1):
	if((arr[i]>arr[i-1]) and (arr[i]>arr[i+1])):
		count +=1
	
print(count)