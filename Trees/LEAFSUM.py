class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def sumofleafnodes(self, root):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return root.data
        
        leftsum = self.sumofleafnodes(root.left)
        rightsum = self.sumofleafnodes(root.right)

        return leftsum + rightsum

tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

leaf_sum = tree.sumofleafnodes(tree.root)
print(f"Sum of leaf nodes: {leaf_sum}")