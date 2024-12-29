class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def rootnode(root):
        if root:
            print(f"root node: {root.data}")

    def leafnode(root):
        if root is None:
            return
        
        if root.left is None and root.right is None:
            print(f"leaf node : {root.data}")
        
        Node.leafnode(root.left)
        Node.leafnode(root.right)

    def findnode(root, value):
        if root is None:
            return
        if root.data == value:
            return root
        left_result = Node.findnode(root.left, value)
        if left_result:
            return left_result

        return Node.findnode(root.right, value)
    
    def finddepth(root, node, level = 0):
        if root is None:
            return -1
        if root.data == node:
            return level
        left_depth = Node.finddepth(root.left, node, level+1)
        if left_depth != -1:
            return left_depth
        
        return Node.finddepth(root.right, node, level+1)
    
    def findheight(root):
        if root is None:
            return -1
        left_height = Node.findheight(root.left)
        right_height = Node.findheight(root.right)

        return 1 + max(left_height, right_height)


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

Node.rootnode(root)
Node.leafnode(root)

print(Node.findnode(root,40).data)

print(Node.finddepth(root,50))

print(Node.findheight(root))