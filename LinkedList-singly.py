class Nodes:
    def __init__(self,data):
        self.dataval=data
        self.nextval=None

class LinkedList:
    def __init__(self):
        self.headval=None
    def traverse(self):
        currentnode=self.headval
        while currentnode is not None:
            print(currentnode.dataval)
            currentnode=currentnode.nextval
    def insert_beginning(self,item):
        newnode=Nodes(item)
        newnode.nextval =self.headval
        self.headval=newnode
    def insert_end(self,item):
        newnode = Nodes(item)
        if self.headval is None:
            self.headval=newnode
            return
        currentnode=self.headval
        while currentnode.nextval is not None:
            currentnode=currentnode.nextval
        currentnode.nextval=newnode
    def insert_inbetween(self,node,item):
        if node is None:
            print("Node does not exist")
        else:
            newnode=Nodes(item)
            newnode.nextval=node.nextval
            node.nextval=newnode
    def removeNode(self,item):
        currentnode=self.headval
        prevnode=None
        if self.headval==item:
            self.headval=self.headval.nextval
            return
        while currentnode is not None:
            if currentnode.dataval==item:
                prevnode.nextval=currentnode.nextval
                break
            prevnode = currentnode
            currentnode=currentnode.nextval
    def find_middleval(self):
        fastpointer=self.headval
        slowpointer=self.headval
        while fastpointer is not None and fastpointer.nextval is not None:
            fastpointer=fastpointer.nextval.nextval
            slowpointer=slowpointer.nextval
            print(slowpointer.dataval)
        print("The middle value is:"+str(slowpointer.dataval))

    def reverse(self):
        current_node = self.headval
        prev=None
        forward=None
        current_node=self.headval
        while(current_node.nextval is not None):
            forward=current_node.nextval
            current_node.nextval=prev
            prev=current_node
            current_node=forward
        self.headval=current_node
        self.headval.next=prev




ll=LinkedList()
ll.insert_beginning("Open Door")
ll.insert_end("Remove Shoes")
ll.insert_end("Place Key")
ll.insert_end("Enjoy!")
ll.insert_beginning("Take out Key")
ll.insert_inbetween(ll.headval.nextval,"Home Home")
#ll.traverse()
#ll.removeNode("Home Home")

ll.traverse()
#print(ll.headval.dataval)
#ll.find_middleval()
ll.reverse()
#print(ll.headval.dataval)
ll.traverse()