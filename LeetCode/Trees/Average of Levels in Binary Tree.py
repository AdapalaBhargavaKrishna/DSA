# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def bfs(root):
            if not root:
                return []

            q = deque([root])
            result = []

            while q:
                level_size = len(q)
                level = []

                for _ in range(level_size):
                    node = q.popleft()
                    level.append(node.val)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                result.append(sum(level) / level_size)
            return result
        return bfs(root)