class Solution(object):
    def sortColors(self, nums):
        for i in range((len(nums))):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i] , nums[j] = nums[j], nums[i]
        return nums
    
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]