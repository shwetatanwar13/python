def merge_sorted_array(l1,l2):
    if l1[-1]<l2[0]:
        l1=l1+l2
    elif l2[-1]<l1[0]:
        l2=l2+l1
    else:
        for i in range(0,len(l1)):
            p=0
            for j in range(0,len(l2)):
                if l1[i]<l2[j]:
                    l2.insert(j,l1[i])
                    p=1
                    break
            if p==0:
                l2.append(l1[i])
    print(l2)
l2=[2,4,6,8]
l1=[1,2,3]
merge_sorted_array(l1,l2)
