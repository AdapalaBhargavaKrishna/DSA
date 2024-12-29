def neighbour(arr, target):
    low = 0
    high = len(arr) - 1

    if target <= arr[0]:
        return arr[0]
    if target >= arr[-1]:
        return arr[-1]
    
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if (target - arr[high]) <= (arr[low] - target):
        return arr[high]
    else:
        return arr[low]

arr = [1, 3, 5, 7, 9]
target = int(input("Enter a number"))

print("Array:", arr)
print("Target:", target)
nearest = neighbour(arr, target)
print("Nearest Neighbor:", nearest)