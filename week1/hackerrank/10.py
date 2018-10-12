arr = []
arr2 = []
names = []
for i in range(int(input())):
name = input()
score = float(input())
arr.append([])
arr[i].append(name)
arr[i].append(score)

mini = arr[0][1]

for i in arr:
if(i[1]<mini):
 mini = i[1]
 

for i in arr:
 if i[1]!=mini:
     arr2.append(i) 

mini = arr2[0][1]

for i in arr2:
if(i[1]<mini):
 mini = i[1]


for i in arr2:
 if i[1] == mini:
     names.append(i[0])

names.sort()
for i in names:
print(i)