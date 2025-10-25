def findContentChildren(g, s):
    g.sort()
    s.sort()

    child = cookie = 0

    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1
        cookie += 1

    return child

g1 = [1, 2, 3]
s1 = [1, 1]
print(findContentChildren(g1, s1))  # Output: 1

g2 = [1, 2]
s2 = [1, 2, 3]
print(findContentChildren(g2, s2))  # Output: 2

g3 = [10, 9, 8, 7]
s3 = [5, 6, 7, 8]
print(findContentChildren(g3, s3))  # Output: 2
