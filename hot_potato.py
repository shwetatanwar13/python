import Queue

def hot_potato():
    cir=Queue.Queue()
    cir.enqueue(4)
    cir.enqueue(3)
    cir.enqueue(2)
    cir.enqueue(1)
    num=int(raw_input("Enter the number: "))
    i=0
    while cir.size()!=1:
         i=0
         while i<num:
          cir.enqueue(cir.dequeue())
          i=i+1
         cir.dequeue()
    return cir.dequeue()

print(hot_potato())