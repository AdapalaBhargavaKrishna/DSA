class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def rootNode(self):
        return self.root.data
    
    def printleafNodes(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            print(f"Leaf Node : ", root.data)

        self.printleafNodes(root.left)
        self.printleafNodes(root.right)

    def findNode(self, root, value):
        if root is None:
            return None
        if root.data == value:
            return root

        leftresult = self.findNode(root.left, value)
        if leftresult:
            return leftresult

        return self.findNode(root.right, value)

    def finddepth(self, root, node, level = 0):
        if root is None:
            return -1
        if root == node:
            return level
        
        leftdepth = self.finddepth(root.left, node, level + 1)
        if leftdepth != -1:
            return leftdepth
        return self.finddepth(root.right, node, level + 1)

    def findheight(self, node):
        if node is None:
            return -1
        leftheight = self.findheight(node.left)
        rightheight = self.findheight(node.left)
        return 1 + max( leftheight, rightheight)
    
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# Root node
tree.rootNode()

# Leaf nodes
print("\nLeaf nodes:")
tree.printleafNodes(tree.root)

# Find node
value = 5
node = tree.findNode(tree.root, value)
if node:
    print(f"\nNode with value {value} found.")
else:
    print(f"\nNode with value {value} not found.")

# Find depth of a node
depth_of_node = tree.finddepth(tree.root,  tree.root.right.left)
print(f"\nDepth of node {tree.root.right.left.data}: {depth_of_node}")

# Find the height of the tree
height = tree.findheight(tree.root)
print(f"\nHeight of the tree: {height}")
