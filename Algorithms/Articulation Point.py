def find_components(graph, V):
    visited = [False] * V
    components = []

    def dfs(u, comp):
        visited[u] = True
        comp.append(u)
        for v in graph[u]:
            if not visited[v]:
                dfs(v, comp)

    for u in range(V):
        if not visited[u]:
            comp = []
            dfs(u, comp)
            components.append(comp)

    return components

def articulation_points(graph, V):
    visited = [False] * V
    disc = [float('inf')] * V
    low = [float('inf')] * V
    parent = [-1] * V
    ap = [False] * V
    time = [0]

    def dfs(u):
        children = 0
        visited[u] = True
        disc[u] = low[u] = time[0]
        time[0] += 1

        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                dfs(v)

                low[u] = min(low[u], low[v])

                if parent[u] == -1 and children > 1:
                    ap[u] = True
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True

            elif v != parent[u]:
                low[u] = min(low[u], disc[u])

    for u in range(V):
        if not visited[u]:
            dfs(u)

    return [u for u in range(V) if ap[u]]

graph = {
    0 : [1],
    1 : [0, 2, 3],
    2 : [1],
    3 : [1, 4],
    4 : [3]
}

components = find_components(graph, 5)
aps = articulation_points(graph, 5)

print("Connected Components")
for comp in components:
    print(comp)

print("Articulation Points:", aps)

# Connected Components
# [0, 1, 2, 3, 4]
# Articulation Points: [1, 3]
      
# 0 --- 1 --- 3 --- 4
#       |
#       2