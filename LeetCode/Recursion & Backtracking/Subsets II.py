def subsetsWithDup(nums):
    nums.sort()
    result = []

    def backtrack(idx, path):
        result.append(path[:])

        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result

print(subsetsWithDup([1, 2, 2]))
# Output:
# [
#   [], [1], [1, 2], [1, 2, 2],
#   [2], [2, 2]
# ]
print(subsetsWithDup([0]))
# Output: [[], [0]]
print(subsetsWithDup([1, 1]))
# Output: [[], [1], [1, 1]]
print(subsetsWithDup([1, 2, 2, 3]))
# Output: [[], [1], [1,2], [1,2,2], [1,2,3], [1,2,2,3], [1,3], [2], [2,2], [2,3], [2,2,3], [3]]