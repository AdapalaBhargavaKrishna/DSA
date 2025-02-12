#book version
def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        lefthalf =  A[:mid]
        righthalf = A[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
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

#class version
def mergesort(list, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergesort(list, low, mid)
    mergesort(list, mid + 1, high)
    merge(list, low, high, mid)

def merge(list, low, high, mid):
    leftlist = list[low:mid + 1]
    rightlist = list[mid + 1:high + 1]

    lli = 0
    rli = 0
    sort = low

    while lli < len(leftlist) and rli < len(rightlist):
        if leftlist[lli] < rightlist[rli]:
            list[sort] = leftlist[lli]
            lli += 1
        else:
            list[sort] = rightlist[rli]
            rli += 1
        sort += 1

    while lli < len(leftlist):
        list[sort] = leftlist[lli]
        lli += 1
        sort += 1
    
    while rli < len(rightlist):
        list[sort] = rightlist[rli]
        rli += 1
        sort += 1

list = [34,23,4,1,56,2,19,25,16]
list1 = [34,23,4,1,56,2,19,25,16]

low = 0
high = len(list) - 1

mergesort(list, low, high)
print(list)


mergeSort(list1)
print(list1)