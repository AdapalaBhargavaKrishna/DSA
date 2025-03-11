class Solution(object):
    def isHappy(self, n):
        seen = set()

        def get_next(n):
            return sum(int(digit)**2 for digit in str(n))

        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1