def prims(graph, start):
    visited = [False] * len(graph)
    key = [float('inf')] * len(graph)
    key[start] = 0
    result = 0

    for _ in range(len(graph)):
        min_key = float('inf')
        u = -1

        for v in range(len(graph)):
            if not visited[v] and key[v] < min_key:
                min_key = key[v]
                u = v

        visited[u] = True
        result += key[u]

        for v , weight in graph[u]:
            if not visited[v] and weight < key[v]:
                key[v] = weight

    return result

graph = {
    0: [(1, 4), (2, 3)],
    1: [(0, 4), (2, 1), (3, 2)],
    2: [(0, 3), (1, 1), (3, 4)],
    3: [(1, 2), (2, 4)],
}

print(prims(graph, 0))

# 0 --4-- 1
# |      / \
# 3     1   2
# |   /       \
# 2 --------4-- 3

# Node 0: connects to 1 (weight 4), 2 (weight 3)
# Node 1: connects to 0 (weight 4), 2 (weight 1), 3 (weight 2)
# Node 2: connects to 0 (weight 3), 1 (weight 1), 3 (weight 4)
# Node 3: connects to 1 (weight 2), 2 (weight 4)

# Prims MST Total Weight: 6