class Solution(object):
    def runningSum(self, nums):
        run = [0] * len(nums)
        run[0] = nums[0]
        for i in range(1, len(nums)):
            run[i] = run[i - 1] + nums[i]
        return run

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].