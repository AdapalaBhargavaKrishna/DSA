class Solution(object):
    def moveZeroes(self, nums):
        index = 0 

        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1

        while (index < len(nums)):
            nums[index] = 0
            index += 1

        return nums
    
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]