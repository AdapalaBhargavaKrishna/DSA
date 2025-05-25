def shortest_path(v, cost, n):
    INF = float('inf')
    dist = [0] * n
    S = [False] * n
    prev = [-1] * n
    prev[v] = v

    for j in range(n):
        dist[j] = cost[v][j]
        S[j] = False

    S[v] = True
    dist[v] = 0

    for _ in range(n - 1):
        min_dist = float('inf')
        u = -1

        for j in range(n):
            if not S[j] and dist[j] < min_dist:
                min_dist = dist[j]
                u = j

        if u == -1:
            break

        S[u] = True

        for w in range(n):
            if not S[w] and cost[u][w] != INF:
                if dist[w] > dist[u] + cost[u][w]:
                    dist[w] = dist[u] + cost[u][w]
                    prev[w] = u

    for i in range(n):
        path = []
        x = i
        while x != -1 and x != prev[x]:
            path.insert(0, x)
            x = prev[x]
        path.insert(0, v)
        print(f"To {i}: dist = {dist[i]}, path = {' -> '.join(map(str, path))}")

INF = float('inf')

n = 5

cost = [
    [0, 10, INF, 30, 100],
    [10, 0, 50, INF, INF],
    [INF, 50, 0, 20, 10],
    [30, INF, 20, 0, 60],
    [100, INF, 10, 60, 0]
]

source_vertex = 0
shortest_path(source_vertex, cost, n)

# To 0: dist = 0, path = 0
# To 1: dist = 10, path = 0 -> 1
# To 2: dist = 50, path = 0 -> 3 -> 2
# To 3: dist = 30, path = 0 -> 3
# To 4: dist = 60, path = 0 -> 3 -> 2 -> 4