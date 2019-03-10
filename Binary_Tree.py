class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,item):

     if self.data:
        if self.data>item:
            if self.left is None:
             self.left=Node(item)
            else:
             self.left.insert(item)
        elif self.data<item:
            if self.right is None:
              self.right=Node(item)
            else:
                self.right.insert(item)
        else:
            self.data=item

    def traverse(self):
        if self.left:
            self.left.traverse()
        print(self.data)

        if self.right:
            self.right.traverse()
    def search_item(self,item):
        if item <self.data:
            if self.left is None:
                print("Item not found")
            else:
                self.left.search_item(item)
        elif item>self.data:
            if self.right is None:
                print("Item not found")
            else:
                self.right.search_item(item)

        else:
            print("Item found")


def maxDepth(root):

        if root is None:
            return 0
        else:
            # Compute the depth of each subtree
            lDepth = maxDepth(root.left)
            rDepth = maxDepth(root.right)
        return(lDepth if lDepth>rDepth else rDepth)+1


tree=Node(60)
tree.insert(40)
tree.insert(70)
tree.insert(45)
tree.insert(38)
tree.insert(76)
tree.insert(36)
tree.traverse()
print(maxDepth(tree))
