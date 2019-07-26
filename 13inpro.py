n,q = map(int,input().split())
n = list(map(int,input().split()))
for i in range(q):
    b ,e = map(int,input().split())
    imm = sum(n[b-1:e])
    # print(*n[b-1:e])
    print(imm)
