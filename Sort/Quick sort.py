# book version
def quick_sort(A, low, high): 
    if low < high:
        pivot = partition(A, low, high)
        quick_sort(A,low,pivot - 1)
        quick_sort(A,pivot + 1,high)

def partition(A, low , high):
    pivot = A[low]
    left = low + 1
    right = high
    done = False

    while not done:
        while left <= right and A[left] <= pivot:
            left = left + 1
        while A[right] >= pivot and right >= left:
            right = right -1
        
        if right < left:
            done = True
        else:
            temp = A[left]
            A[left] = A[right]
            A[right] = temp
    
    temp = A[low]
    A[low] = A[right]
    A[right] = temp
    return right

# class version
def quicksort(list, low, high):
    if low < high:
        pivot = partition(list, low, high)
        quicksort(list, low, pivot - 1)
        quicksort(list, pivot + 1, high)

def partition(list, low, high):
    i = ( low-1 )
    pivot = list[high]
    
    for j in range(low , high):

        if list[j] <= pivot:
            i = i+1
            list[i],list[j] = list[j],list[i]

    list[i+1],list[high] = list[high],list[i+1]
    return ( i+1 )

list = [6, 3, 2, 1, 5, 4]
list1 = [20, 10, 30, 40, 50, 60, 70, 80, 90, 100]
low = 0
high = len(list) - 1
quicksort(list, low , high)
print(list)
quick_sort(list1, low , high)
print(list1)
