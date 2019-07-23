num=int(input())

l = list(map(int,input().split()))

x = sum(l[:len(l)//2])/len(l[:len(l)//2])

y = sum(l[(len(l)//2)+1:])/len(l[(len(l)//2)+1:])

if x == y:

    print("yes")

else:

    print("no")
