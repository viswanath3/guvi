num = int(input())
b = 0
for i in range(2,num-1):
    if num%i == 0:
    	b=1
    	break
print("yes" if not b else "no")
