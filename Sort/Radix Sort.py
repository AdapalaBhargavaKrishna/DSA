# book version
def radixSort(A):
    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1
    while not maxLength:
        maxLength = True
        buckets = [list() for _ in range(RADIX)]
        for i in A:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                A[a] = i
                a += 1
        placement *= RADIX


# class version
def radixsort(list):
    maxi = max(list)
    pos = 1

    while (maxi//pos > 0):
        counter(list, pos)
        pos *= 10
        
def counter(list, pos):
    count = [0] * 10
    temp = [0] * len(list)

    for i in range(len(list)):
        index = (list[i] // pos) % 10
        count[index] += 1

    for i in range(1, len(count)):
        count[i] = count[i - 1] + count[i]

    for i in range(len(list) - 1, -1, -1):
        index = (list[i] // pos) % 10
        count[index] -= 1
        temp[count[index]] = list[i]

    for i in range(len(list)):
        list[i] = temp[i]
    

l=[10,2,5,80,88,976,45]
l1 = [23,34,45,67,78,89,90]

radixsort(l)
print(l)

radixSort(l1)
print(l1)