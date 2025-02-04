class Solution(object):
    def twoSum(self, nums, target):

        dict_pair = {}
        
        for i ,num in enumerate(nums):
            if target - num in dict_pair:
                return [i, dict_pair[target-num]]
            dict_pair[num] = i