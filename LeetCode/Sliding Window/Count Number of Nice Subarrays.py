class Solution(object):
    def numberOfSubarrays(self, nums, k):
        n = len(nums)

        def atMost(k):
            odd = 0
            count = 0
            left = 0
            for right in range(n):
                if nums[right] % 2 == 1:
                    odd += 1

                while odd > k:
                    if nums[left] % 2 == 1:   
                        odd -= 1
                    left += 1

                count + = right - left + 1

            return count

        return atMost(k) - atMost(k - 1)

# Example 1:
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

# Example 2:
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.