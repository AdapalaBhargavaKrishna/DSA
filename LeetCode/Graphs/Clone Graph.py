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

def printGraph(node):
    seen, q = set(), [node]
    while q:
        n = q.pop(0)
        if n in seen: 
            continue
        seen.add(n)
        print(n.val, "→", [x.val for x in n.neighbors])
        q += [x for x in n.neighbors if x not in seen]


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

print("Original Graph:")
printGraph(n1)
print("\nCloned Graph:")
printGraph(cloned)