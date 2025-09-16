def nthRoot(N, M):
    low, high = 1, M
    
    while low <= high:
        mid = (low + high) // 2
        val = mid ** N
        
        if val == M:
            return mid
        elif val < M:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1


# Example usage
print(nthRoot(3, 27))   # Output: 3
print(nthRoot(4, 69))   # Output: -1
print(nthRoot(2, 16))   # Output: 4
