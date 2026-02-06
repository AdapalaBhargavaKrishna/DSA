class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        total = 0

        for i in range(len(arr)):
            total_sub = (i + 1) * (n - i)
            odds = (total_sub + 1) // 2
            total += arr[i] * odds
        return total

# Example 1:
# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58