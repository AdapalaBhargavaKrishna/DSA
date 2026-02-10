class Solution(object):
    def reverseVowels(self, s):
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -=1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"