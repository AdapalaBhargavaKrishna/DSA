# Given an array of distinct integers and a target, you have to return the list of all unique combinations where the chosen numbers sum to target. You may return the combinations in any order.


def combinationSum(candidates, target):
    res = []

    def dfs(start, path, total):
        if total == target:
            res.append(path[:])
            return
        if total > target or start >= len(candidates):
            return

        path.append(candidates[start])
        dfs(start, path, total + candidates[start])
        path.pop()
        
        dfs(start + 1, path, total)

    dfs(0, [], 0)
    return res