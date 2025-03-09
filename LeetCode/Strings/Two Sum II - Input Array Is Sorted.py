class Solution(object):
    def twoSum(self, numbers, target):
        
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1,  right + 1]

            elif total < target:
                left += 1
            else:
                right -= 1

        return []
    
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].