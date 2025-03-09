class Solution(object):
    def searchRange(self, nums, target):
    
        def findFirst(nus, target):
            left, right = 0 , len(nums) - 1
            first = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= target:
                    right = mid - 1

                else:
                    left = mid + 1
                
                if nums[mid] == target:
                    first = mid
                
            return first

        def findLast(nus, target):
            left, right = 0 , len(nums) - 1
            last = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] <= target:
                    left = mid + 1

                else:
                    right = mid - 1
                
                if nums[mid] == target:
                    last = mid
                
            return last
        
        first = findFirst(nums, target)
        last = findLast(nums, target)
        return [first, last]
    

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]