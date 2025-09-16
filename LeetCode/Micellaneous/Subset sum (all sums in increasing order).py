# Given an array, print all the sum of the subset generated from it, in the increasing order.

def subsetSums(nums):
    res = []

    def dfs(index, total):
        if index == len(nums):
            res.append(total)
            return
        
        dfs(index + 1, total + nums[index])
        
        dfs(index + 1, total)

    dfs(0, 0)
    return sorted(res)

# Test Case 1
nums = [2, 3]
# Subsets: [], [2], [3], [2,3] → sums: 0, 2, 3, 5
print(subsetSums(nums))  # Expected Output: [0, 2, 3, 5]

# Test Case 2
nums = [5, 2, 1]
# Subsets: [], [5], [2], [1], [5,2], [5,1], [2,1], [5,2,1] → sums: 0,5,2,1,7,6,3,8
# Sorted: [0,1,2,3,5,6,7,8]
print(subsetSums(nums))  # Expected Output: [0, 1, 2, 3, 5, 6, 7, 8]

# Test Case 3: Single element
nums = [10]
# Subsets: [], [10] → sums: 0, 10
print(subsetSums(nums))  # Expected Output: [0, 10]

# Test Case 4: Empty array
nums = []
# Subsets: [] → sum: 0
print(subsetSums(nums))  # Expected Output: [0]

# Test Case 5: Array with negative numbers
nums = [1, -2, 3]
# Subsets sums: 0, 1, -2, 3, -1, 4, 1, 2 → sorted: [-2, -1, 0, 1, 1, 2, 3, 4]
print(subsetSums(nums))  # Expected Output: [-2, -1, 0, 1, 1, 2, 3, 4]
