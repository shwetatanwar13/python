def bubble_sort(l):
    for i in range(len(l)):
        for j in range(1,len(l)-i):
            if l[j-1]>l[j]:
                l[j-1],l[j]=l[j],l[j-1]
    print(l)

bubble_sort([0,1,2,1,1,2,0,0,2])