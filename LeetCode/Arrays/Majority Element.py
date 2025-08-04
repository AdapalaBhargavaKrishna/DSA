class Solution(object):
    def majorityElement(self, nums):
        numbers = {}
        max_num = len(nums) // 2

        for num in nums:
            if num  in numbers:
                numbers[num] += 1
            else:
                numbers[num] = 1

            if numbers[num] > max_num:
                return num

class Solution(object):
    def majorityElement(self, nums):
        numset = set(nums)

        for i in numset:
            if nums.count(i) > (len(nums) // 2):
                return i
        return -1

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2