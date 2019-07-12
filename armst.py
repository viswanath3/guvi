k=int(input())
h=list(map(int,str(k)))
j=list(map(lambda x:x**3,h))
if(sum(j)==k):
    print("yes")
else:
    print("no")
