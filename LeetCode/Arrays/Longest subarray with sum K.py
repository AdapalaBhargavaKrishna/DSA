class Solution:
    def longestSubarray(self, nums, k):
    
        numsmap = {}
        maxlen = 0
        current_sum = 0

        for index , num in enumerate(nums):
            current_sum += num

            if current_sum == k:
                maxlen = index + 1

            if current_sum - k in numsmap:
                subarray_length = index - numsmap[current_sum - k]
                maxlen = max(maxlen, subarray_length)

            if current_sum not in numsmap:
                numsmap[current_sum] = index

        return maxlen
    
# Input: nums = [10, 5, 2, 7, 1, 9],  k=15
# Output: 4
# Explanation:
# The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.

# Input: nums = [-3, 2, 1], k=6
# Output: 0
# Explanation:
# There is no sub-array in the array that sums to 6. Therefore, the output is 0.