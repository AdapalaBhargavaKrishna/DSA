def min_max(arr, i, j, min, max):
    if i == j:
        min = max = arr[i]
    elif i == j - 1:
        if arr[i] < arr[j]:
            min = arr[i]
            max = arr[j]
        else:
            min = arr[j]
            max = arr[i]
    else:
        mid = (i + j) // 2
        min1, max1 = min_max(arr, i, mid, min, max)
        min2, max2 = min_max(arr, mid + 1, j, min, max)

        if max1 < max2:
            max = max2
        else:
            max = max1
        
        if min1 < min2:
            min = min1
        else:
            min = min2
            
    return min,max

arr = list(map(int, input().split()))
mini, maxi = min_max(arr, 0, len(arr) - 1, min, max)
print(arr)
print(f"minimum: {mini}")
print(f"maximum: {maxi}")