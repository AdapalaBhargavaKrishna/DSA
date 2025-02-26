class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        rows = [""] * numRows
        index = 0
        step = 1

        for char in s:
            rows[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step

        return "".join(rows)

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I