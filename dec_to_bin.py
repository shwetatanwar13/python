import stack as s

st=int(raw_input("enter the decimal number: "))
x=s.Stack()
q=st
while q != 0:
    r=q%2
    q=q//2
    x.push(r)
i=x.size()
bin=''
while i > 0:
    bin= bin + str(x.peek())
    x.pop()
    i=i-1
print(bin)


