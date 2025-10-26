def canFinish(numCourses, prerequisites):
    adj = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for a, b in prerequisites:
        adj[b].append(a)
        indegree[a] += 1

    queue = []
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)

    completed = 0
    while queue:
        course = queue.pop(0)
        completed += 1

        for nei in adj[course]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    return completed == numCourses

print(canFinish(2, [[1,0]]))            # True
print(canFinish(2, [[1,0],[0,1]]))      # False
print(canFinish(4, [[1,0],[2,1],[3,2]])) # True
print(canFinish(3, [[0,1],[1,2],[2,0]])) # False
print(canFinish(5, []))                  # True