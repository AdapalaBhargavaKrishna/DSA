class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(root, data):
        if root is None:
            return BST(data)
        if data < root.data:
            root.left = BST.insert(root.left, data)
        else:
            root.right = BST.insert(root.right, data)
        return root
    
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=" ")
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.data, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=" ")

root = BST(50)

# Insert nodes into the tree
root.insert(30)
root.insert(70)
root.insert(20)
root.insert(40)
root.insert(60)
root.insert(80)

root.inorder()
print()
root.preorder()
print()
root.postorder()
print()