class Solution(object):
    def canJump(self, nums):
        maxjump = 0
        for i in range(len(nums)):
            if i > maxjump:
                return False
            maxjump = max(maxjump, i + nums[i])
            if maxjump >= len(nums) - 1:
                return True
        return True
    
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.