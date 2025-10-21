class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        result = []

        def backtrack(idx , path):
            
            result.append(path[:])

            for i in range(idx ,len(nums)):

                if i > idx and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result
    
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
