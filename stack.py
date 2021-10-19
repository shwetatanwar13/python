class Stack:
    def __init__(self):
        self.item = list();

    def pop(self):
        self.item.pop()

    def peek(self):
        return self.item[len(self.item)-1]

    def size(self):
         return (len(self.item))

    def push(self,n):
         self.item.append(n)

    def is_empty(self):
         return(len(self.item)==0)

