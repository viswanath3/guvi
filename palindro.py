num=int(input())
temp=num
sum=0
while num>0:
	digit=num%10
	sum=sum*10+digit
	num=num//10
if temp==sum:
	print("yes")
else:
	print("no")
	
