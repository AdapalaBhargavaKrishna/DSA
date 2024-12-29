list = [6, 3, 2, 1, 5, 4]
low = 0
high = len(list) - 1

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

quicksort(list, low , high)
print(list)






# def partition(l, low, high):
#     i=low
#     j=high
#     pivot=l[low]

#     while(i<=j):
#         while(i<=high and l[i]<=pivot):
#             i+=1
#         while(l[j]>pivot):
#             j-=1

#     if(i<j):
#       l[i],l[j]=l[j],l[i]


#     l[low],l[j]=l[j],l[low]
#     return j