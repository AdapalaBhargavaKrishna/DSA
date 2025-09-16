# Given an array of N integers. Every number in the array except one appears twice. Find the single number in the array.
def singleNumber(nums):
        res = 0
        for num in nums:
            res = res ^ num
        
        return res

# Test Case 1
print(singleNumber([2, 2, 1]))  
# Expected Output: 1

# Test Case 2
print(singleNumber([4, 1, 2, 1, 2]))  
# Expected Output: 4

# Test Case 3
print(singleNumber([1]))  
# Expected Output: 1

# Test Case 4
print(singleNumber([7, 3, 5, 3, 5]))  
# Expected Output: 7

# Test Case 5
print(singleNumber([10, 20, 10, 30, 30]))  
# Expected Output: 20
