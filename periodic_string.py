import re
s='11111111'
d=dict()
sl=0
n=0
st=''
for i in range(0,int(len(s)/2)):
    t=len(re.findall(s[0:i+1],s))
    if sl<len(s[0:i+1]) and t>1 and (len(s)%t==0):
        sl=len(s[0:i+1])
        st=s[0:i+1]
        n=t
if n!=0:
 print(st)
 print(n)
else:
  print('not periodic')