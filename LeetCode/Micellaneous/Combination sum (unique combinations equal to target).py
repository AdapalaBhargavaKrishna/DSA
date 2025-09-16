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

# Test Case 1
candidates = [2, 3, 6, 7]
target = 7
# Valid combinations: [7], [2,2,3]
print(combinationSum(candidates, target))
# Expected Output: [[2, 2, 3], [7]]

# Test Case 2
candidates = [2, 3, 5]
target = 8
# Valid combinations: [3,5], [2,2,2,2], [2,3,3]
print(combinationSum(candidates, target))
# Expected Output: [[2,2,2,2], [2,3,3], [3,5]]

# Test Case 3
candidates = [2]
target = 1
# No combination possible
print(combinationSum(candidates, target))
# Expected Output: []

# Test Case 4
candidates = [1]
target = 1
# Only one combination: [1]
print(combinationSum(candidates, target))
# Expected Output: [[1]]

# Test Case 5
candidates = [1, 2]
target = 4
# Valid combinations: [1,1,1,1], [1,1,2], [2,2]
print(combinationSum(candidates, target))
# Expected Output: [[1,1,1,1], [1,1,2], [2,2]]