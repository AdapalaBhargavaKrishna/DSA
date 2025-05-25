def is_safe(v, pos, path, graph):
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
        if is_safe(v, pos, path, graph):
            path[pos] = v
            find_cycles(graph, path, pos + 1, V, total)
            path[pos] = -1

def hamiltonian_cycle(graph):
    V = len(graph)
    path = [-1] * V
    path[0] = 0
    total = []

    find_cycles(graph, path, 1, V, total)

    if not total:
        print("No Hamiltonian cycles found.")
        return []
    else:
        print("All Hamiltonian cycles:")
        for cycle in total:
            print(' -> '.join(str(n+1) for n in cycle))
        return total

graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

hamiltonian_cycle(graph)

#     A
#    / \
#   B———C
#   |   |
#   D———E
# All Hamiltonian cycles:
# 1 -> 2 -> 3 -> 5 -> 4 -> 1
# 1 -> 4 -> 5 -> 3 -> 2 -> 1