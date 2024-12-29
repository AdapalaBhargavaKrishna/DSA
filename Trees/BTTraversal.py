class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end = " ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end = " ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data , end = " ")

tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("In-order traversal:")
tree.inorder(tree.root)
print("\nPre-order traversal:")
tree.preorder(tree.root)
print("\nPost-order traversal:")
tree.postorder(tree.root)