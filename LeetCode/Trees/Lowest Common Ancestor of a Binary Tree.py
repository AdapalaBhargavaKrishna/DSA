class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    
    return left if left else right

root = TreeNode(3 , TreeNode(5 , TreeNode(6) , TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))

p = root.left          # 5
q = root.right         # 1
print(lowestCommonAncestor(root, p, q).val)  # Output: 3

p = root.left          # 5
q = root.left.right.right  # 4
print(lowestCommonAncestor(root, p, q).val)  # Output: 5

root2 = TreeNode(1)
root2.left = TreeNode(2)
p = root2
q = root2.left

print(lowestCommonAncestor(root2, p, q).val)  # Output: 1
