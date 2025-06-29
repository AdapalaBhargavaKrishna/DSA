class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        index = {}
        for i , num in enumerate(nums):
            if num in index and i - index[num] <= k:
                return True
            index[num] = i
        return False

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true