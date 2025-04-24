def is_safe(vertex, graph, color, c, v):
    for i in range(v):
        if graph[vertex][i] == 1 and color[i] == c:
            return False
    return True

def coloring(graph, m, color, vertex, V):
    if vertex == V:
        return True 
    
    for c in  range(1, m + 1):
        if is_safe(vertex, graph, color, c, V):
            color[vertex] = c
            if coloring(graph, m, color, vertex + 1, V):
                return True
            color[vertex] = 0
    return False


def graph_coloring(graph, m):
    V = len(graph)
    color = [0] * V
    if not coloring(graph, m, color, 0, V):
        print("Solution does not exist")
        return False
    
    print(color)
    
    for i in range(V):
        print(f"vertex {i + 1} -> color {color[i]}")

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

m = 3
graph_coloring(graph, m)