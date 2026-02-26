class Solution(object):
    def minSwaps(self, s):
        b = 0
        ib = 0
        for c in s:
            if c == '[':
                b += 1
            else:
                b -= 1
            ib = min(ib,b)
        return (-ib+1) // 2