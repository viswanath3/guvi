def prime(j):
    v = 0
    for vi in range(2,j-1):
        if j%vi == 0:
            v=1
            break
    if not v:
        print(j,end=" ")

d ,e = map(int,input().split())
l =[]
for x in range(d+1,e):
    prime(x)
