class Solution(object):
    def lengthOfLastWord(self, s):
        word = s.strip().split()
        return len(word[-1]) if word else 0
    
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.