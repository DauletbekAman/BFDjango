from math import*
v = int(input())
t = int(input())
s = v*t

if(v>=0):
	
	if (s<109):
		print(s)
	

	else:	
	   while (s>=109):
	    s= s-109
	   print(s)

else:

	if(s>-109):
		print((109+s))

	else:
		while(s<-109):
			s = s + 109
		print(109+s)
	







		 
		
