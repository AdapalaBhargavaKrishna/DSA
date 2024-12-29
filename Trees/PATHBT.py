class BST:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    def insert(root,data):
        if root is None:
            return BST(data)

        if data<root.data:
            root.left=BST.insert(root.left,data)
        if data>root.data:
            root.right=BST.insert(root.right,data)
        return root

    def findpath(self, node, path = []):
        if self is None:
            return False
        path.append(self.data)

        if self.data == node:
            return True
        
        if self.left:
            if self.left.findpath(node, path):
                return True
            
        if self.right:
            if self.right.findpath(node, path):
                return True
        
        path.pop()
        return False
    

root = BST(5)
root.insert(3)
root.insert(7)
root.insert(2)
root.insert(4)
root.insert(6)
root.insert(8)

find = 4
path = []

if root.findpath(find, path ):
    print(f"Path from root to node {find}: {' -> '.join(map(str, path))}")
else:
    print(f"Node {find} not found in the tree.")



