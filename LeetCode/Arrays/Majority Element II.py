class Solution(object):
    def majorityElement(self, nums):
        freq = {}
        condition = len(nums) // 3
        result = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for num in freq:
            if freq[num] > condition:
                result.append(num)

        return result
    

# Example 1:
# Input: nums = [3,2,3]
# Output: [3]

# Example 2:
# Input: nums = [1]
# Output: [1]