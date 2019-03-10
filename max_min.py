a=[2,1,4,7,5,9]

maxnum=0
minnum=999
for i in a:
    if i>maxnum:
     maxnum=i
    elif i<minnum:
      minnum=i

print((maxnum,minnum))