class Solution:
    def reverse(self, x: int) -> int:
        int_max, int_min = 2**31 - 1, -2**31
        res = 0

        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:
            digit = x % 10
            x = x // 10

            if res > (int_max - digit) // 10:
                return 0

            res = res * 10 + digit

        return sign * res