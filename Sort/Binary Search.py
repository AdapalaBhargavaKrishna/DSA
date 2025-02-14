# book version
def binarySearch(list, value):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == value:
            return mid
        elif list[mid] < value:
            low = mid + 1
        elif list[mid] > value:
            high = mid - 1
    return -1

# class version
def binary(list, val, low, high):
    if low > high:
        return
    
    mid = (low + high) // 2

    if list[mid] == val:
        print(f"{val} found at index {mid}")
    elif list[mid] > val:
        return binary(list, val, low , mid - 1)
    elif list[mid] < val:
        return binary(list, val, mid + 1, high)
    else:
        print(f"{val} not found")

l=[2,5,3,4,6,7]
l1=[5,4,3,2,1]
l.sort()
l1.sort()
print(l)
print(l1)
key=5
low=0
high=len(l)-1
binary(l,key,low,high)
print(binarySearch(l1,key))