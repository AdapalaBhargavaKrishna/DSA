list = [10, 24, 16, 18, 29, 17]

n = len(list)

for i in range(0,n - 1):
    min = i
    for j in range(i + 1, n):
        if list[min] > list[j]:
            min = j
    list[i] , list[min] = list[min] , list[i]

print(list)