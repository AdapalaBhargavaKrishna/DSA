def canFinish(numCourses, prerequisites):
    preMap={i:[] for i in range(numCourses)}

    for crs,pre in prerequisites:
        preMap[crs].append(pre)
    
    visited=set()
    cycle=set()

    def dfs(crs):
        if crs in cycle:
            return False
        
        if crs in visited:
            return True
        
        if preMap[crs]==[]:
            return True
        
        cycle.add(crs)
        
        for pre in preMap[crs]:
            if not dfs(pre):return False
        
        cycle.remove(crs)
        visited.add(crs)
        preMap[crs]=[]
        return True
    
    for crs in range(numCourses):
        if not dfs(crs):return False
    
    return True
    
print(canFinish(2, [[1,0]]))            # True
print(canFinish(2, [[1,0],[0,1]]))      # False
print(canFinish(4, [[1,0],[2,1],[3,2]])) # True
print(canFinish(3, [[0,1],[1,2],[2,0]])) # False
print(canFinish(5, []))                  # True