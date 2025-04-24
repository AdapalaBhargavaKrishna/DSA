def is_safe(v, pos, path, graph, V):
    if graph[path[pos - 1]][v] == 0:
        return False
    if v in path:
        return False
    return True

def find_cycle(graph, path, pos, V):
    if pos == V:
        return graph[path[pos - 1]][path[0]] == 1
    
    for v in range(1, V):
        if is_safe(v, pos, path, graph, V):
            path[pos] = v
            if find_cycle(graph, path, pos + 1, V):
                return True 
            path[pos] = -1

    return False


def hamiltonion_cycle(graph):
    V = len(graph)
    path = [-1] * V
    path[0] = 0

    if not find_cycle(graph, path, 1, V):
        print("No Hamiltonian Cycle found")
        return None
    else:
        path.append(path[0])
        print("Hamiltonion cycle found")
        print("->".join(map(str, path)))
        return path

graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

hamiltonion_cycle(graph)