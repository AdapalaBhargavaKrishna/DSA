class Solution(object):
    def divisorSubstrings(self, num, k):
        left = 0
        right = k
        num_str = str(num)
        count = 0

        while right <= len(num_str):
            int_num = int(num_str[left:right])
            left += 1
            right += 1
            if int_num !=0 and num % int_num == 0:
                count += 1
        return count

# Example 1:
# Input: num = 240, k = 2
# Output: 2
# Explanation: The following are the substrings of num of length k:
# - "24" from "240": 24 is a divisor of 240.
# - "40" from "240": 40 is a divisor of 240.
# Therefore, the k-beauty is 2.

# Example 2:
# Input: num = 430043, k = 2
# Output: 2
# Explanation: The following are the substrings of num of length k:
# - "43" from "430043": 43 is a divisor of 430043.
# - "30" from "430043": 30 is not a divisor of 430043.
# - "00" from "430043": 0 is not a divisor of 430043.
# - "04" from "430043": 4 is not a divisor of 430043.
# - "43" from "430043": 43 is a divisor of 430043.
# Therefore, the k-beauty is 2.