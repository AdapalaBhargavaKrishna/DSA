#Find Minimum in Rotated Sorted Array

class Solution(object):
    def findMin(self, nums):
        
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1

            else:
                right = mid

        return nums[left]
    
# You must write an algorithm that runs in O(log n) time.
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.