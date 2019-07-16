no = input()
k= list(map(int,input().split()))
c = True
for j in k:
    if k.count(j) > 1:
        c= False
        break
print(j if c else "unique")
