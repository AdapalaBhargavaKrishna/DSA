def findOrder(numCourses, prerequisites):
    preMap={i:[] for i in range(numCourses)}

    for crs,pre in prerequisites:
        preMap[crs].append(pre)
    
    visited=set()
    cycle=set()
    output=[]

    def dfs(crs):
        if crs in cycle:
            return []
        
        if crs in visited:
            return True
        
        cycle.add(crs)

        for pre in preMap[crs]:
            if not dfs(pre): return False
        
        cycle.remove(crs)
        visited.add(crs)
        output.append(crs)
        return True
    
    for crs in range(numCourses):
        if dfs(crs)==False:
            return []
    
    return output

print(findOrder(2, [[1,0]]))            # [0,1]
print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]])) # [0,1,2,3] or [0,2,1,3]
print(findOrder(1, []))                  # [0]
print(findOrder(2, [[0,1],[1,0]]))       # [] (cycle)
