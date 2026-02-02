class Solution(object):
    def totalFruit(self, fruits):
        left = 0
        right = 0
        count = {}
        maxLen = 0

        while right < len(fruits):

            count[fruits[right]] = count.get(fruits[right], 0) + 1

            if len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
            else:
                maxLen = max(maxLen, right - left + 1)
            
            right += 1
        return maxLen

class Solution(object):
    def totalFruit(self, fruits):
        left = 0
        right = 0
        count = {}
        maxLen = 0

        while right < len(fruits):

            count[fruits[right]] = count.get(fruits[right], 0) + 1

            if len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
            else:
                maxLen = max(maxLen, right - left + 1)
            
            right += 1
        return maxLen


# Example 1:
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.

# Example 2:
# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].

# Example 3:
# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].