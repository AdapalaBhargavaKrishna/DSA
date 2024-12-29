class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

class BinaryTree:
    def __init__(self):
        self.root = None

    def kth_level(self, root, k):
        if root is None:
            return
        
        if k == 0:
            print(root.data , end = " ")

        else:
            self.kth_level(root.left, k - 1)
            self.kth_level(root.right, k - 1)

tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

k = 2
print(f"Nodes at level {k}:")
tree.kth_level(tree.root, k)