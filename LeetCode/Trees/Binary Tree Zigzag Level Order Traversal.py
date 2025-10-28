class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    if not root:
        return []
    
    q = [root]
    res = []
    left_to_right = True

    while q:
        level = []
        for _ in range(len(q)):
            node = q.pop(0)
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        if not left_to_right:
            level.reverse()
        
        res.append(level)
        left_to_right = not left_to_right
    
    return res

root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(zigzagLevelOrder(root1))  # [[3], [20, 9], [15, 7]]
root2 = TreeNode(1)
print(zigzagLevelOrder(root2))  # [[1]]
root3 = None
print(zigzagLevelOrder(root3))  # []