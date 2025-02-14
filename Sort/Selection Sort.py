def selectionSort(list):
    for i in range(len(list) - 1, 0 , -1):
        maxi = 0
        for j in range(1, i + 1):
            if list[j] > list[maxi]:
                maxi = j
        list[i], list[maxi] = list[maxi], list[i]

list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(list)
print(list)