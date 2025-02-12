def insertionSort(A):
    for i in range(1, len(A)):
        temp = A[i]
        k = i
        while k > 0 and temp < A[k - 1]:
            A[k] = A[k - 1]
            k -= 1
        A[k] = temp

A = [64, 34, 25, 12, 22, 11, 90]
insertionSort(A)
print("Sorted array is:", A)