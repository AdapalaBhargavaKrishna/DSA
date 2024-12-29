l = [1,2,3,4,6,7,8,9,10]

pos = int(input("Enter a number"))
n = int(input("Enter a number"))

l.append(None)

low = 0
high = len(l) - 1

while low <= high:
    mid = (low + high) // 2

    if mid == pos:
        for i in range(len(l) - 1, mid, -1):
            l[i] = l[i - 1]
        l[pos] = n
        break
    elif mid > pos:
        high = mid - 1
    elif mid < pos:
        low = mid + 1

print(l)