from collections import OrderedDict
def non_repeater(s):

    d=OrderedDict()
    for i in range(0,len(s)):
        for j in range(i+1,len(s)):
           d[s[j]]=0
           if s[j]==s[i]:
               d[s[j]]=1
               break
    for k,v in d.items():
        if v==0:
            print(k)
            break

non_repeater("swiss")