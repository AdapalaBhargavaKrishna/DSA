class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        num = 0
        for i in range(len(s) + 1):
            if s[num:i] in wordDict:
                dp[i] = True
                num = i
        return dp[-1]

# ai
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        n = len(s) + 1
        dp = [False] * n
        dp[0] = True

        for i in range(1, n):
            for j in range(i):
                if dp[j] and s[j:i] in wordset:
                    dp[i] = True
                    break
        return dp[n - 1]