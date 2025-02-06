#Longest Palindromic Substring

class Solution(object):
    def longestPalindrome(self, s):

        if not s:
            return ""

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        ans = ""
        for i in range(len(s)):
            odd_palindrome = expand(i,i)
            if len(odd_palindrome) > len(ans):
                ans = odd_palindrome

            even_palindrome = expand(i, i + 1)
            if len(even_palindrome) > len(ans):
                ans = even_palindrome

        return ans