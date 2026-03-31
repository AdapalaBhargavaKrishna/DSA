class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        rows , cols = len(matrix) , len(matrix[0])

        low = 0
        high = (rows * cols) - 1

        while low <= high:
            mid = low + (high - low) // 2
            mid_val = matrix[mid // cols][mid % cols]

            if mid_val == target:
                return True

            elif mid_val < target:
                low = mid + 1
            
            else:
                high = mid - 1
        return False
