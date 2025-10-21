class Solution(object):
    def subsets(self, nums):

        result = [[]]

        for num in nums:
            result += [curr + [num] for curr in result]
        return result
    
class Solution(object):
    def subsets(self, nums):
        result = []

        def backtrack(idx , path):
            result.append(path[:])
            for i in range(idx ,len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
    
        return result
    
# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]