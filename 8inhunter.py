no= input()
ok = list(map(int,input().split()))
for k in range(len(ok)):
    for x in range(len(ok)):
        for n in range(len(ok)):
            if ok[k]+ok[x] == ok[n] and k<x<n:
                print(ok[k],ok[x],ok[n])
