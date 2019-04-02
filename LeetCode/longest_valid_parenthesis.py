from collections import OrderedDict
j=0
T=int(input())
while(j < T):
       d=OrderedDict()
       A=input()
       print(A)
       for i in A:
           if i in d.keys():
             d[i]+=1
           else:
             d[i]=1
       if d['(']==d[')']:
           l=list(d)
           counter=d['(']+d[')']
           if l[0]=='(':
               print(counter)
       j+=1


