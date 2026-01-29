class Solution(object):
    def sortArrayByParity(self, nums):
        slow = 0
        
        for fast in range(len(nums)):
            if nums[fast] % 2 == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return nums

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]