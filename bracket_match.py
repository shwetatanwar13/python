import stack as s

st=raw_input("enter the string: ")
x=s.Stack()
flag=True
for i in st:
    if i in ('(','{','[') :
        x.push(i)
    else:
        if x.is_empty():
            flag = False
            break
        elif (x.peek()=='(' and i ==')') or (x.peek()=='{' and i =='}') or (x.peek()=='[' and i ==']'):
            x.pop()
        else:
            flag = False
            break
print("The input string is balanced" if x.is_empty()and flag==True else "Unbalanced string")
