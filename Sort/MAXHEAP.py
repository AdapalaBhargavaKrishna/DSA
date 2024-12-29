def maxheap(list, n):
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(list, n, i)

def heapify(list, n, i):
    l = 2*i + 1
    r = 2*i + 2

    large = i

    if l < n and list[l] > list[large]:
       large = l    
    if r < n and list[r] > list[large]:
       large = r
    if large != i:
        list[large],list[i] = list[i],list[large]
        heapify(list, n, large)

list=[4,3,1,5,7,6]
n=len(list)
maxheap(list,n)
print(list)