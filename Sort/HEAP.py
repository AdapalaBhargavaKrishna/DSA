def heap(list, n):
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(list, n, i)

    for i in range(n - 1, 0 , -1):
        list[i],list[0] = list[0], list[i]
        heapify(list, i, 0)

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
heap(list,n)
print(list)