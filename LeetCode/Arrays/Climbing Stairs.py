class Solution(object):
    def climbStairs(self, n):
        
        if n <= 2:
            return n

        first = 1
        second = 2

        for i in range(3, n + 1):
            third = first  + second
            first = second
            second = third

        return second
    
# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step