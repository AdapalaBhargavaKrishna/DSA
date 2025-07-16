class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        
        while n%2 == 0:
            n = n//2

        return n == 1
    
# Example 1:
# Input: n = 1
# Output: true
# Explanation: 20 = 1

# Example 2:
# Input: n = 16
# Output: true
# Explanation: 24 = 16