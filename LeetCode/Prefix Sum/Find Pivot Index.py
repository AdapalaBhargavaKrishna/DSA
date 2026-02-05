class Solution(object):
    def pivotIndex(self, nums):
        n = len(nums)
        prefix = [0] * n

        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i - 1] + nums[i]

        total = prefix[-1]

        for i in range(n):
            left =  prefix[i - 1] if i > 0 else 0
            right = total - prefix[i]

            if left == right:
                return i

        return -1

# Example 1:
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# Example 2:
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.