# Given an integer array arr of size N, sorted in ascending order (with distinct values) and a target value k. Now the array is rotated at some pivot point unknown to you. Find the index at which k is present and if k is not present return -1.

def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# Example 1
nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))  # Output: 4

# Example 2
nums = [4,5,6,7,0,1,2]
target = 3
print(search(nums, target))  # Output: -1

# Example 3
nums = [1]
target = 0
print(search(nums, target))  # Output: -1

# Additional Test Case 1: target is the first element
nums = [6,7,1,2,3,4,5]
target = 6
print(search(nums, target))  # Output: 0

# Additional Test Case 2: target is the last element
nums = [6,7,1,2,3,4,5]
target = 5
print(search(nums, target))  # Output: 6

# Additional Test Case 3: array not rotated
nums = [1,2,3,4,5,6,7]
target = 4
print(search(nums, target))  # Output: 3

# Additional Test Case 4: array of size 2, rotated
nums = [2,1]
target = 1
print(search(nums, target))  # Output: 1

# Additional Test Case 5: array of size 2, not rotated
nums = [1,2]
target = 2
print(search(nums, target))  # Output: 1
