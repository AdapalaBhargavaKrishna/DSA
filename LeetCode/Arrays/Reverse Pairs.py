class Solution(object):
    def reversePairs(self, nums):
        def merge_sort(arr, left, right):
            if left >= right:
                return 0

            mid = (left + right) // 2
            count = merge_sort(arr, left , mid) + merge_sort(arr, mid + 1 , right)

            j = mid + 1

            for i in range(left, mid + 1):
                while j <= right and arr[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)

            temp = []

            i , j = left, mid + 1

            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1

                else:
                    temp.append(arr[j])
                    j += 1
            
            while i <= mid:
                temp.append(arr[i])
                i += 1

            while j <= right:
                temp.append(arr[j])
                j += 1

            for i in range(len(temp)):
                arr[ left + i ] = temp[i]

            return count 

        return merge_sort(nums, 0, len(nums) - 1)
    
# Example 1:
# Input: nums = [1,3,2,3,1]
# Output: 2
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1

# Example 2:
# Input: nums = [2,4,3,5,1]
# Output: 3
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
# (2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1