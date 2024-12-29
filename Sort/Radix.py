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
radixsort(l)
print(l)