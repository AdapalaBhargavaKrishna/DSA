def krushkals(V, edges):
    parent = list(range(V))
    rank = [0] * V

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(u, v):
        pu, pv = find(u), find(v)

        if pu == pv:
            return False

        if rank[pu] < rank[pv]:
            parent[pu] = pv
        elif rank[pv] < rank[pu]:
            parent[pv] = pu
        else:
            parent[pv] = pu
            rank[pu] += 1
            
        return True

    edges.sort(key=lambda x: x[2])
    weight = 0

    for u, v, w in edges:
        if union(u, v):
            weight += w

    return weight

edges = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
]

print("Kruskal's MST Total Weight:", krushkals(4, edges))

#      4
#    0 ---- 1
#    |    / |
#   3| 1/   |2
#    | /    |
#    2 ---- 3
#      4

# Kruskal's MST Total Weight: 6