class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if not root:
        return []
    
    q , res = [root] , []

    while q:
        level = []
        for _ in range(len(q)):
            node = q.pop(0)
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    
    return res

root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(levelOrder(root1))  # [[3], [9, 20], [15, 7]]

root2 = TreeNode(1)
print(levelOrder(root2))  # [[1]]

root3 = None
print(levelOrder(root3))  # []