import stack as s

x=s.Stack()
x.push(10)
print(x.peek())
x.push('abc')
print(x.peek())
x.push(-1)
print(x.peek())
print(x.pop())
print(x.peek())
print(x.pop())
print(x.pop())
print(x.is_empty())