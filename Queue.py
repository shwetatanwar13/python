class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return (len(self.items))
    def isEmpty(self):
        return (len(self.items)==0)
q=Queue()
q.enqueue('fat')
q.enqueue('cat')
print(q.items)
q.enqueue('dog')
print(q.items)
q.dequeue()
print(q.items)