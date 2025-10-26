class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    if not root:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(inorderTraversal(root))  # Output: [1, 3, 2]

root = TreeNode(1,
                TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
                TreeNode(3, None, TreeNode(8, TreeNode(9), None)))
print(inorderTraversal(root))  # Output: [4,2,6,5,7,1,3,9,8]

print(inorderTraversal(None))  # Output: []
print(inorderTraversal(TreeNode(1)))  # Output: [1]
