class Solution(object):
    def minOperations(self, nums, x):
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        if target < 0:
            return - 1

        left = 0
        curr_sum = 0
        max_len = -1

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum > target and left <= right:
                curr_sum -= nums[left]
                left += 1
            
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)

        return len(nums) - max_len

# Example 1:
# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

# Example 2:
# Input: nums = [5,6,7,8,9], x = 4
# Output: -1