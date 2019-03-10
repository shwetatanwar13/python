import math
def permutations(s):
    s=list(s)
    perm_no=math.factorial(len(s))
    count=0
    l=[]
    print(len(s))
    for i in range(0,perm_no):
        s[count],s[count+1]=s[count+1],s[count]
        s1=(''.join(i for i in s))
        l.append(s1)
        if (count+1)==(len(s)-1):
            count=0
        else:
            count = count + 1

    print(l)

permutations('xyzw')