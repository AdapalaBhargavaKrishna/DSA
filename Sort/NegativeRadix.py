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
        index = (list[i]//pos) % 10
        count[index] += 1

    for i in range(1, len(count)):
        count[i] = count[i - 1] + count[i]

    for i in range(len(list) - 1, -1, -1):
        index = (list[i] // pos) % 10
        count[index] -= 1
        temp[count[index]] = list[i]

    for i in range(len(list)):
        list[i] = temp[i]

def negatives(list):
    negative = [-num for num in list if num < 0]
    positive = [num for num in list if num >= 0]

    if negative:

        radixsort(negative)
        negative = [-num for num in reversed(negative)]
    
    if positive:
        radixsort(positive)

    return negative + positive

l = [-170, 45, -75, 90, 802, -24, 2, -66]
print("Original array:", l)
l = negatives(l)
print("Sorted array:", l)