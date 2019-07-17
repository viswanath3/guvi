def get_comon_prefix_len(len,list1,list2):
    common_len = 0
    for j in range(len):
        if list1[j]==list2[j]:
            common_len+=1
        else:
            break
    return common_len

x = int(input())
l,cl = [],[]
for x in range(x):
    l.append(list(input()))
# print(len(l))
for x in range(len(l)):
    if x != len(l)-1:   
        # print("i count:",i)
        list1,list2 = l[x],l[x+1]
        list1_len , list2_len = len(list1),len(list2)
        if list1_len < list2_len:
            common_len = get_comon_prefix_len(list1_len,list1,list2)
        else:
            common_len = get_comon_prefix_len(list2_len,list1,list2)
        # print("common len",common_len," for list ",list1,list2)
        cl.append(common_len)
        # print("#"*30)
print("".join(list1[:common_len]))
