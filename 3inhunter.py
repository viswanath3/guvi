null =input()
lis = input().split()
reg = []
for j in range(len(lis)):
    if str(j) == lis[j]:
        reg.append(lis[j])
print(" ".join(reg) if len(reg) > 0 else "-1")
