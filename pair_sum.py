a=[2, 4, 7, 5, 9, 10, -1]
s=9
final=set()
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
      if a[i]+a[j]==s:
        final.add((a[i],a[j]))
print(sorted(final))

