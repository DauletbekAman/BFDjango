n = int(input())
arr = []
count = 0
for i in range(n):
	arr.append(int(input()))


for i in range(n):
	if(arr[i]<0):
		count +=1
print(count)