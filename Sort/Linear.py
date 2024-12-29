def lsearch(arr, size, val):
    if size == 0:
        return -1
    if arr[size - 1] == val:
        return size - 1
    else:
        return lsearch(arr, size - 1, val)

l = [1,2,3,4,5,6,7,8,9,10]

size = len(l)
print(lsearch(l, size, 6))