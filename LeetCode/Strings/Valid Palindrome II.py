class Solution(object):
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1
        if len(s) <= 1:
            return True
        while(left < right):
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                s1 = s[left +1 : right+1]
                s2 = s[left : right]
                return s1 == s1[::-1] or s2 == s2[::-1]
        return True

# Example 1:
# Input: s = "aba"
# Output: true

# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.