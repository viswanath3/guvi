import collections as c
avail = input()
n = list(map(int,input().split()))
acr = c.Counter(n)
same = []
for item,counting in acr.items():
    if counting >1 :
        same.append(item)
if same:
    print(*same)
else:
    print("unique")
n
