def is_safe(vertex, graph, color, c, v):
    for i in range(v):
        if graph[vertex][i] == 1 and color[i] == c:
            return False
        
    return True

def coloring(graph, m, color, vertex, V, solutions):
    if vertex == V:
        solutions.append(color[:])
        return
    
    for c in range(1, m + 1):
        if is_safe(vertex, graph, color, c, V):
            color[vertex] = c
            coloring(graph, m, color, vertex + 1, V, solutions)
            color[vertex] = 0

def graph_coloring(graph, m):
    V = len(graph)
    color = [0] * V
    solutions = []
    coloring(graph, m, color, 0, V, solutions)
 
    if not solutions:
        print("No solutions exist with", m, "colors.")
    else:
        print(f"All possible colorings with {m} colors:")
        for idx, solution in enumerate(solutions, 1):
            print(f"Solution {idx}: ", end="")
            for i in range(V):
                print(f"\nvertex {i + 1} -> color {solution[i]}", end="; ")
            print()

    for sol in solutions:
        print(sol)

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

m = 3
graph_coloring(graph, m)

#     A
#    /|\
#   B | D
#    \|/
#     C

# Solution 1: vertex 1 -> color 1; vertex 2 -> color 2; vertex 3 -> color 3; vertex 4 -> color 2; 
# Solution 2: vertex 1 -> color 1; vertex 2 -> color 3; vertex 3 -> color 2; vertex 4 -> color 3; 
# Solution 3: vertex 1 -> color 2; vertex 2 -> color 1; vertex 3 -> color 3; vertex 4 -> color 1; 
# Solution 4: vertex 1 -> color 2; vertex 2 -> color 3; vertex 3 -> color 1; vertex 4 -> color 3; 
# Solution 5: vertex 1 -> color 3; vertex 2 -> color 1; vertex 3 -> color 2; vertex 4 -> color 1; 
# Solution 6: vertex 1 -> color 3; vertex 2 -> color 2; vertex 3 -> color 1; vertex 4 -> color 2; 
# [1, 2, 3, 2]
# [1, 3, 2, 3]
# [2, 1, 3, 1]
# [2, 3, 1, 3]
# [3, 1, 2, 1]
# [3, 2, 1, 2]