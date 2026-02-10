class Solution(object):
    def reverseStr(self, s, k):
        n = len(s)
        s = list(s)
        for i in range(0,n, 2*k):
            s[i:i + k] = reversed(s[i : i + k])
        return ''.join(s)

# Example 1:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

# Example 2:
# Input: s = "abcd", k = 2
# Output: "bacd"