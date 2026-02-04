class Solution(object):
    def subarraySum(self, nums, k):
        result = 0
        prefix_sum = 0
        mp = {0 : 1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in mp:
                result += mp[prefix_sum - k]
            mp[prefix_sum] = mp.get(prefix_sum, 0) + 1
            
        return result

# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2