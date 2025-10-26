def permute(nums):
    res = []

    def backtracking(path, used):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            if i not in used:
                path.append(nums[i])
                used.add(i)
                backtracking(path, used)
                path.pop()
                used.remove(i)

    backtracking([], set())
    return res

print(permute([1, 2, 3]))
# Output: [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

print(permute([0, 1]))  # [[0,1], [1,0]]
print(permute([1]))     # [[1]]