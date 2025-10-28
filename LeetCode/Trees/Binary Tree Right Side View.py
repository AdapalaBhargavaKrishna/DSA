class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    if not root:
        return []
    
    q , res = [root] , []

    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.pop(0)
            if i == level_size - 1:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    
    return res

root1 = TreeNode(1)
root1.left = TreeNode(2, None, TreeNode(5))
root1.right = TreeNode(3, None, TreeNode(4))
print(rightSideView(root1))  # [1, 3, 4]

root2 = TreeNode(1)
root2.left = TreeNode(2, TreeNode(4, TreeNode(5)))
root2.right = TreeNode(3)
print(rightSideView(root2))  # [1, 3, 4, 5]

root3 = TreeNode(1, None, TreeNode(3))
print(rightSideView(root3))  # [1, 3]

root4 = None
print(rightSideView(root4))  # []