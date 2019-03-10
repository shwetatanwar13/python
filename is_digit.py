s='1234'
for i in s:
    s=0
    if (not i.isdigit()):
        print("not all characters digit")
        s=1
        break
if s==0:
    print("All chracters digit")
