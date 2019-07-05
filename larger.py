num1,num2,num3=map(int,input().split())
if(num1>=num2) and (num1>=num3):
 	maxi=num1
elif(num2>=num1) and (num2>=num3):
	maxi=num2
else:
 	maxi=num3
print(maxi)	
