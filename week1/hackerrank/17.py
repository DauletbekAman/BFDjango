s = input()

count=0
for i in range(len(s)):
    count=0
    if(s[i].isalnum()):
        print(True)
        count+=1
        break
if count==0:
    print(False)    

 
       
for i in range(len(s)):
    count=0
    if(s[i].isalpha()):
        print(True)
        count+=1
        break
if count==0:
    print(False)
    
   
for i in range(len(s)):
    count=0
    if(s[i].isdigit()):
        print(True)
        count+=1
        break
if count==0:
    print(False)
       
for i in range(len(s)):
    count=0
    if(s[i].islower()):
        print(True)
        count+=1
        break
if count==0:
    print(False)
       
for i in range(len(s)):
    count=0
    if(s[i].isupper()):
        print(True)
        count+=1
        break
if count==0:
    print(False)
    