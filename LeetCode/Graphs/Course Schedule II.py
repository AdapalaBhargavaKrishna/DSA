def findOrder(numCourses, prerequisites):
    adj = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for a, b in prerequisites:
        adj[b].append(a)
        indegree[a] += 1

    queue = []
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)

    order = []
    i = 0
    while i < len(queue):
        course = queue[i]
        i += 1
        order.append(course)

        for nei in adj[course]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    return order if len(order) == numCourses else []

print(findOrder(2, [[1,0]]))            # [0,1]
print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]])) # [0,1,2,3] or [0,2,1,3]
print(findOrder(1, []))                  # [0]
print(findOrder(2, [[0,1],[1,0]]))       # [] (cycle)
