class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        left = 0
        n = len(nums)
        total = 0
        ans = 1

        for right in range(n):
            total += nums[right]

            while nums[right] * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans

# Example 1:
# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment 1 to 2 and 2 to 4. 3 operations.

# Example 2:
# Input: nums = [1,4,8,13], k = 5
# Output: 2
# Explanation: Increment 1 to 4. 3 operations.