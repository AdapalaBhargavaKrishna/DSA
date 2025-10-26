def subsets(nums):
    result = []

    def backtrack(idx, path):
        result.append(path[:])

        for i in range(idx, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result

print(subsets([1, 2, 3]))
# Output:
# [
#   [], 
#   [1], [1, 2], [1, 2, 3], [1, 3],
#   [2], [2, 3],
#   [3]
# ]
print(subsets([0]))
# Output: [[], [0]]
print(subsets([]))
# Output: [[]]