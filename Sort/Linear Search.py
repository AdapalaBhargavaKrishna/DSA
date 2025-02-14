# iterative
def linearsearch(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return i
        elif list[i] > value:
            return -1
    return -1

# recursive
def lsearch(arr, size, val):
    if size == 0:
        return -1
    if arr[size - 1] == val:
        return size - 1
    else:
        return lsearch(arr, size - 1, val)

l = [1,2,3,4,5,6,7,8,9,10]
l1 = [3, 14, 27, 31, 42, 55, 63, 74, 86, 95]
print(lsearch(l, len(l), 6))
print(linearsearch(l1, 74))