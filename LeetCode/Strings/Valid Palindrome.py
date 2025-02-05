class Solution(object):
    def isPalindrome(self, s):
        result = ''.join(char.lower() for char in s if char.isalnum())
        return result == result[::-1]