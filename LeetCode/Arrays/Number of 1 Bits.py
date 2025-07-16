class Solution(object):
    def hammingWeight(self, n):
        count = 0

        while (n > 0):
            if n & 1:
                count += 1
            n = n >> 1

        return count

# Example 1:
# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits.

# Example 2:
# Input: n = 128
# Output: 1
# Explanation:
# The input binary string 10000000 has a total of one set bit.