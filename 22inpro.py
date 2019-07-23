cons = int(input())

esum,osum = 0,0

l = list(map(int,input().split()))

for i in range(cons):

    if i%2 == 0:

        esum+=l[i]

    else:

        osum+=l[i]

print(esum , osum)
