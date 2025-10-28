class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    def helper(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        
        if not (low < node.val < high):
            return False
        
        return (helper(node.left, low, node.val) and
                helper(node.right, node.val, high))    
    return helper(root)

root1 = TreeNode(2, TreeNode(1), TreeNode(3))
print(isValidBST(root1))  # True
root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print(isValidBST(root2))  # False
root3 = TreeNode(1)
print(isValidBST(root3))  # True
root4 = TreeNode(10, TreeNode(5, TreeNode(2), TreeNode(7, TreeNode(6))), TreeNode(15))
print(isValidBST(root4))  # False