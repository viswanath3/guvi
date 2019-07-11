def facto(i):
   if i== 0 or 1:
   	   return 1
   else:
   	   return i*facto(i-1)
   	
n=int(input())   	
print(facto(n))
