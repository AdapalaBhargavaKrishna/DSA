class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        current_sum = 0

        for num in nums:
            current_sum += num
            max_sum = max(max_sum , current_sum)
            if current_sum < 0:
                current_sum = 0

        return max_sum

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.