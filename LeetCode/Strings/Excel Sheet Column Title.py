class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        temp = columnNumber
        res = ''
        while temp > 0:
            temp -= 1
            res += chr((temp % 26) + 65)
            temp //= 26

        return res[::-1]