def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j] , arr[j + 1] = arr[j + 1] , arr[j]

arr = [3, 6, 1, 8, 4, 5]
print("Original array:", arr)

bubblesort(arr)
print("Sorted array in descending order:", arr)