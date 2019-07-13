pr= []
def primee(i):
    d = 0
    for j in range(2,i-1):
        if i%j == 0:
            d =1
            break
    if not d:
        pr.append(i)

c ,en = map(int,input().split())

for k in range(c,en+1):
    primee(k)
print(len(pr))
