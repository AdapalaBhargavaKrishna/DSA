def minheap(list, n):
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(list, n, i)

def heapify(list, n , i):
    small = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and list[l] < list[small]:
        small = l
    if r < n  and list[r] < list[small]:
        small = r

    if small != i:
        list[small],list[i] = list[i], list[small]
        heapify(list, n, small)
    
list = [4,3,1,5,7,6]
n = len(list)
minheap(list, n)
print(list)