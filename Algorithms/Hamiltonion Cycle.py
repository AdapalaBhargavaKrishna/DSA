def is_safe(v, pos, path, graph, V):
    if graph[path[pos - 1]][v] == 0:
        return False
    if v in path:
        return False
    return True

def find_cycles(graph, path, pos, V, total):
    if pos == V:
        if graph[path[pos - 1]][path[0]] == 1:
            total.append(path[:] + [path[0]])
        return
    
    for v in range(1, V):
        if is_safe(v, pos, path, graph, V):
            path[pos] = V
            find_cycles(graph, path, pos + 1, V, total)
            path[pos] = -1


def hamiltonion_cycle(graph):
    V = len(graph)
    path = [-1] * V
    path[0] = 0
    total = []

    find_cycles(graph, path, 1, V, total)


graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

hamiltonion_cycle(graph)