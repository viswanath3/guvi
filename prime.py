num = int(input())
n = 0
for i in range(2,num-1):
    if num%i == 0:
    	n=1
    	break
print("yes" if not n else "no")
