class Solution(object):
    def twoSum(self, nums, target):

        dict_pair = {}
        
        for i ,num in enumerate(nums):
            if target - num in dict_pair:
                return [i, dict_pair[target-num]]
            dict_pair[num] = i

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].