# You are given a string s, partition it in such a way that every substring is a palindrome. Return all such palindromic partitions of s.

def partition(s):
    res = []

    def isPalindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):
            res.append(path[:])
            return
        
        for end in range(start + 1, len(s) + 1):
            if isPalindrome(s[start: end]):
                path.append(s[start: end])
                backtrack(end, path)
                path.pop()

    backtrack(0, [])
    return res

s="aab"
print(partition(s)) # [['a', 'a', 'b'], ['aa', 'b']]




def partition(s):
    res = []

    dp = [[False] * len(s) for _ in range(len(s))]

    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j] and (j - i <= 2 or dp[i  + 1][j - 1]):
                dp[i][j] = True



    def backtrack(start, path):
        if start == len(s):
            res.append(path[:])
            return
        
        for end in range(start, len(s)):
            if dp[start][end]:
                path.append(s[start: end + 1])
                backtrack(end + 1, path)
                path.pop()

    backtrack(0, [])
    return res

s="aab"
print(partition(s))
