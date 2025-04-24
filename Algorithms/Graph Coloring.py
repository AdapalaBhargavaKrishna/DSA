def is_safe(vertex, graph, color, c, V):
    for i in range(V):
        if graph[vertex][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, vertex, V):
    if vertex == V:
        return True

    for c in range(1, m + 1):
        if is_safe(vertex, graph, color, c, V):
            color[vertex] = c
            if graph_coloring_util(graph, m, color, vertex + 1, V):
                return True
            color[vertex] = 0  # Backtrack
    return False

def graph_coloring(graph, m):
    V = len(graph)
    color = [0] * V
    if not graph_coloring_util(graph, m, color, 0, V):
        print("Solution does not exist")
        return False
    
    print(color)
    
    # for i in range(V):
    #     print(f"vertex {i + 1} -> color {color[i]}")
    # return True

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

m = 3  # Number of colors
graph_coloring(graph, m)
