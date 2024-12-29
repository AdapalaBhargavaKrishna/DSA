class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BT:
    def __init__(self):
        self.root = None

    def nodes(self, root):
        if root is None:
            return 0
        
        leftcount = self.nodes(root.left)
        rightcount = self.nodes(root.right)

        return 1 + leftcount + rightcount
    
    def leafs(self, root):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        return self.leafs(root.left) + self.leafs(root.right)
    
tree = BT()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

total_nodes = tree.nodes(tree.root)
print(f"Total number of nodes: {total_nodes}")

leaf_nodes = tree.leafs(tree.root)
print(f"Number of leaf nodes: {leaf_nodes}")