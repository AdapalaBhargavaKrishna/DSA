def dfs(graph, node):
    
    visited = []
    stack = []

    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        print(s)
        for x in graph[s][::-1]:
            if x not in visited:
                visited.append(x)
                stack.append(x)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A')