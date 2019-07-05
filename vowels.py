list_a=['a','e','i','o','u']
list_b=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
char=str(input())
if(char in list_a):
    print("Vowels")
elif(char in list_b):
    print("Consonant")
else:
    print("invalid")
