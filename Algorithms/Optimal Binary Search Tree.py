def optimalBST(freq, keys, i, j, root):
    if i == j:
        return 0

    if i == j - 1:
        root[i][j] = i
        return freq[i]

    c = {}
    for k in range(i,j):
        left = optimalBST(freq, keys, i, k, root)
        right = optimalBST(freq, keys, k + 1, j, root)
        w = sum(freq[i:j])

        c[k] = left + right+ w

    k_min = min(c, key = c.get)
    root[i][j] = k_min
    return c[k_min]

def printT(keys, root, i, j, parent=None):
    if i >= j:
        return 
    
    r = root[i][j]

    if parent is None:
        print(f"root is {keys[r]}")
    else:
        print(f"{keys[r]} is child of {keys[parent]}")

    printT(keys, root, i, r, r)
    printT(keys, root, r + 1, j, r)

freq = [4, 2, 6, 3]
keys = [10, 20, 30, 40]
n = len(keys)
root = [[-1] * (n + 1) for _ in range (n + 1)]

cost = optimalBST(freq, keys, 0, n, root)
printT(keys, root, 0, n)

print(f"cost of BST : {cost}")

for k in root:
    print(k)