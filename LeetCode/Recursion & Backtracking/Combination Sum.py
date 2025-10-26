def combinationSum(candidates, target):
    res = []

    def dfs(start, path, total):
        if total == target:
            res.append(path[:])
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            dfs(i, path, total + candidates[i])
            path.pop()

    dfs(0, [], 0)
    return res

print(combinationSum([2, 3, 6, 7], 7))
# Output: [[2, 2, 3], [7]]
print(combinationSum([2, 3, 5], 8))
# Output: [[2,2,2,2],[2,3,3],[3,5]]
print(combinationSum([2], 1))
# Output: []
print(combinationSum([1], 2))
# Output: [[1,1]]
print(combinationSum([1], 1))
# Output: [[1]]