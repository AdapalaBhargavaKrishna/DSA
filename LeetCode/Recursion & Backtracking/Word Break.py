def wordBreak(s, wordDict):
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]

print(wordBreak("leetcode", ["leet","code"]))      # True
print(wordBreak("applepenapple", ["apple","pen"])) # True
print(wordBreak("catsandog", ["cats","dog","sand","and","cat"])) # False
print(wordBreak("aaaaaaa", ["aaa","aaaa"]))        # True