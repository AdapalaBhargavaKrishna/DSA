class Solution(object):
    def countSubstrings(self, s):

        n = len(s)
        count = 0

        for i in range(n):
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        
        return count

# Example 1:
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".