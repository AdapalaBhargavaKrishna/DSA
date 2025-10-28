class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    diameter = [0]

    def dfs(node):
        if not node:
            return 0
        
        left_height = dfs(node.left)
        right_height = dfs(node.right)
        
        diameter[0] = max(diameter[0], left_height + right_height)
        
        return 1 + max(left_height, right_height)
    
    dfs(root)
    return diameter[0]

root1 = TreeNode(1)
root1.left = TreeNode(2, TreeNode(4), TreeNode(5))
root1.right = TreeNode(3)
print(diameterOfBinaryTree(root1))  # Output: 3

root2 = TreeNode(1, TreeNode(2))
print(diameterOfBinaryTree(root2))  # Output: 1
