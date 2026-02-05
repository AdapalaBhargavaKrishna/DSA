class Solution(object):
    def checkSubarraySum(self, nums, k):
        remainder = {0:-1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            
            rem = prefix_sum % k if k != 0 else prefix_sum
            if rem in remainder:
                if  i - remainder[rem] >= 2:
                    return True
            else:
                remainder[rem] = i
        return False

class Solution(object):
    def checkSubarraySum(self, nums, k):
        remainder = {0:-1}
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            rem = prefix_sum % k
            if rem in remainder:
                if  i - remainder[rem] >= 2:
                    return True
            else:
                remainder[rem] = i
        return False

# Example 1:
# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

# Example 2:
# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.