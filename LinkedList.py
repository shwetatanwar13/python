from Node import Node
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp

    def traverse(self):
        current = self.head
        while current is not None:
             print(current.data)
             current=current.next
    def size(self):
        current = self.head
        count = 0
        while current is not None:
           count = count+1
           current = current.next
        return count

    def search(self, item):
        current = self.head
        pos = 0
        found = False
        while current is not None:
            if current.data == item:
                found = True
                break
            pos = pos + 1
            current = current.next
        print('The itm is at pos ' + str(pos) if found else 'Item not present')

    def remove(self, item):
        prev = None
        current = self.head
        found = False
        while current is not None:
            if current.data == item:
                if prev == None:
                    self.head = current.next
                elif current.next == None:
                    prev.next = None
                else:
                    prev.next = current.next
                found = True
                break
            else:
                prev = current
                current = current.next

        print('The itm at pos is removed.' if found else 'Item not present')

    def append(self, item):
        current = self.head
        while current.next is not None:
            current = current.next

        if current == None:
            temp = Node(item)
            temp.next = None
            self.head = temp
        else:
            temp = Node(item)
            current.next = temp
            temp.next = None

    def insert(self,pos,item):
        current = self.head
        count = 0
        temp = Node(item)
        found = False
        if self.head == None:
           print("empty linked list")
           return
        while count < pos-1 and current.next is not None:
            current = current.next
            count = count+1
            found = True
        if found or current.next is not None:
            temp.next = current.next
            current.next = temp
        else:
           print("position greater than length of linked list")

    def reverse(self):
        current = self.head
        prev = None
        while current is not None:
            temp = current
            if current.next == None:
             self.head = current
            current = current.next
            temp.next = prev
            prev = temp



l=LinkedList()
l.add(31)
l.add(42)
l.add(65)
#l.add(45)
#l.traverse()
#print(l.size())
#l.search(31)
#l.remove(6)
#l.traverse()
#l.append(30)
#l.traverse()
l.insert(1,41)
l.traverse()
l.reverse()
print("after reversing")
l.traverse()

