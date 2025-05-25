def mergesort(A):
    if len(A) > 1:
        mid = len(A) // 2
        lefthalf = A[:mid]
        righthalf = A[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        i = j = k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                A[k] = lefthalf[i]
                i += 1
            else:
                A[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            A[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            A[k] = righthalf[j]
            j += 1
            k += 1

list = [34,23,4,1,56,2,19,25]
mergesort(list)
print(list)

# [1, 2, 4, 19, 23, 25, 34, 56]