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
l.sort()
print(l)
key=5
low=0
high=len(l)-1
binary(l,key,low,high)