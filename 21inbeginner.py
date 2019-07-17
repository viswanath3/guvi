def progresssion(a,b,c):
    s =(/2)*((2*b)+(a-1)*c)
    return int(s)

x = list(map(int,input().split()))
print(progresssion(x[0],x[1],x[2]))
