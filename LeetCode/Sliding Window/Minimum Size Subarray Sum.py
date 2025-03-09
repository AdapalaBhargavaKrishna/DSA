class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                min_length = min(min_length, right - left + 1)
                sum -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.