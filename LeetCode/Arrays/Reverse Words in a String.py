class Solution(object):
    def reverseWords(self, s):
        words = s.strip().split()
        output =""

        for word in reversed(words):
            output += word + " "

        return output.strip()
            
class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])
    
# Input: s = "the sky is blue"
# Output: "blue is sky the"