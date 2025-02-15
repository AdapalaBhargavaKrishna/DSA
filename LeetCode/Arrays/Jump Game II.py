class Solution(object):
    def jump(self, nums):
        if len(nums) <= 0:
            return 0
        
        jumps = 0
        farthest = 0
        steps = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == steps:
                jumps += 1
                steps = farthest
            
                if steps >= len(nums) - 1:
                    break
        return jumps
    
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.