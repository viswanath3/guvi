no  =input()
k = list(map(int,input().split()))
for i in range(len(k)):
    if (i%2 == 0 and k[i]%2 !=0) or (i%2!= 0 and k[i]%2 == 0):
        print(k[i],end = " ")
