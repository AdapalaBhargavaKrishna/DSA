class Solution(object):
    def searchMatrix(self, matrix, target):

        if not matrix:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1

        while low <= high:

            mid = (low + high) // 2
            mid_val = matrix[mid // cols][mid % cols]

            if mid_val == target:
                return True

            elif mid_val < target:
                low = mid + 1

            else:
                high = mid - 1

        return False
    
# Example 1:

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false