class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    if not root:
        return []
    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)

def preorderTraversal(root):
    if not root:
        return []

    stack, result = [root], []

    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result

root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
print(preorderTraversal(root1))  # Output: [1, 2, 3]

root2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(preorderTraversal(root2))  # Output: [1, 2, 4, 5, 3]

root3 = None
print(preorderTraversal(root3))  # Output: []

root4 = TreeNode(1)
print(preorderTraversal(root4))  # Output: [1]