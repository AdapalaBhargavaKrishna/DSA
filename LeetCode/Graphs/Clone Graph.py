class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    if not node:
        return None

    visited = {}

    def dfs(n):
        if n in visited:
            return visited[n]

        copy = Node(n.val)
        visited[n] = copy

        for nei in n.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy

    return dfs(node)


# Build graph: 1 -> [2,4], 2 -> [1,3], 3 -> [2,4], 4 -> [1,3]
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

cloned = cloneGraph(n1)
print(cloned.val)       # 1
print([n.val for n in cloned.neighbors])  # [2, 4] 