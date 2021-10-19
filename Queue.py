class Queue:
    def __init__(self):
        self.q = []


    def enqueue(self, item):
        #self.q.insert(0,item)
        self.q[0:0]=[item]

    def dequeue(self):
        return self.q.pop()

    def size(self):
        return len(self.q)

    def is_empty(self):
        return (True if len(self.q) ==0 else False)