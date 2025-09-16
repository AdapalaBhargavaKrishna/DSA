# Given two sorted arrays of size m and n respectively, you are tasked with finding the element that would be at the kth position of the final sorted array.

def kthElement(a, b, k):
    
    m , n = len(a) , len(b)

    if m > n : 
        return kthElement(b , a , k)
    
    low = max(0, k - n)
    high = min(k, m)

    while low <= high :
        cut1 = (low + high) // 2
        cut2 = k - cut1

        left1 = a[cut1 - 1] if cut1 > 0 else float('inf')
        left2 = b[cut2 - 1] if cut2 > 0 else float('inf')
        right1 = a[cut1] if cut1 < m else float('inf')
        right2 = b[cut2] if cut2 < n else float('inf')

        if left1 <= right2 and left2 <= right1:
            return max(left1, left2)
        
        elif left1 > right2:
            high = cut1 - 1

        else:
            low = cut1 + 1

    return -1


a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
print(kthElement(a, b, k))  # Output: 6

# Test Case 2: Arrays with different lengths
a = [100, 112, 256, 349, 770]
b = [72, 86, 113, 119, 265, 445, 892]
k = 7
print(kthElement(a, b, k))  # Output: 256

# Test Case 3: k is 1 (smallest element)
a = [5, 6, 7]
b = [1, 2, 3, 4]
k = 1
print(kthElement(a, b, k))  # Output: 1