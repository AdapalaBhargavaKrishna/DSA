class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        mp = {0 : 1}
        prefix = 0
        count = 0

        for num in nums:
            prefix += num

            if prefix - goal in mp:
                count += mp[prefix - goal]

            if prefix in mp:
                mp[prefix] += 1
            else:
                mp[prefix] = 1
        return count

# Example 1:
# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]

# Example 2:
# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15