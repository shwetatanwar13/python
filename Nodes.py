class Nodes:
    def __init__(self,data):
        self.data=data
        self.nextval=None

n1=Nodes("Open Door")
n2=Nodes("Remove Shoes")
n3=Nodes("Place Key")
n4=Nodes("Enjoy!")

n1.nextval=n2
n2.nextval=n3
n3.nextval=n4

currentnode=n1
while currentnode:
    print(currentnode.data)
    currentnode=currentnode.nextval