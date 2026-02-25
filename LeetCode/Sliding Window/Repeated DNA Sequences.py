def findRepeatedDnaSequences(s):
    if len(s) < 10:
        return []

    seen = set()
    repeated = set()

    for i in range(len(s) - 9):
        sub = s[i : i + 10]
        if sub in seen:
            repeated.add(sub)
        else:
            seen.add(sub)
    return repeated

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
res = findRepeatedDnaSequences(s)

print(list(res))