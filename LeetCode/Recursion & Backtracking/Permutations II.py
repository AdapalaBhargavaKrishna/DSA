def permuteUnique(nums):
    nums.sort()   
    res = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            path.append(nums[i])
            used[i] = True
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return res

print(permuteUnique([1,1,2]))
# [[1,1,2],[1,2,1],[2,1,1]]
print(permuteUnique([1,2,3]))
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(permuteUnique([2,2,1,1]))
# [[1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]]