class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root):
    if not root:
        return []
    stack, output = [root], []
    
    while stack:
        node = stack.pop()
        output.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return output[::-1]

root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
print(postorderTraversal(root1))  # [3, 2, 1]

root2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(postorderTraversal(root2))  # [4, 5, 2, 3, 1]

root3 = None
print(postorderTraversal(root3))  # []

root4 = TreeNode(1)
print(postorderTraversal(root4))  # [1]
