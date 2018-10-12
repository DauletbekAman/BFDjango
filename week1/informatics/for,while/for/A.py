a = int(input())
b = int(input())

# for i in range(a,b+1):
# 	if(i%2==0):
# 		print(i,end=' ')

if(a%2==0):
 for i in range(a,b+1,2):
  print(i,end=' ')

else:
   for i in range(a+1,b+1,2):
   	print(i,end=' ')
