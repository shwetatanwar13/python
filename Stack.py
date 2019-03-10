class Stack:
    def __init__(self):
        self.items=[]
    def pop(self):
        return self.items.pop()
    def push(self,item):
        return self.items.append(item)
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items)-1]
    def isEmpty(self):
        return (len(self.items)==0)

s=Stack()
s.push(1)
s.push(2)
print(s.peek())
print(s.size())
s.pop()
print(s.size())
print(s.isEmpty())
