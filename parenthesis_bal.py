import stack as s

st=raw_input("enter the string: ")
x=s.Stack()
flag=True
for i in st:
    if i == '(':
        x.push(i)
    else:
        if x.is_empty():
            flag=False
            break
        else:
            x.pop()
print("The input string is balanced" if x.is_empty()and flag==True else "Unbalanced string")
