class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        result = []
        n = len(pattern)
        def check(s):
            if len(s) != n:
                return False
            hs = {}
            hp = {}
            for i in range(n):
                a = s[i]
                b = pattern[i]

                if a in hs and hs[a] != b:
                    return False    
                if b in hp and hp[b] != a:
                    return False
                    
                hs[a] = b
                hp[b] = a
            return True
            
        for word in words:
            if check(word):
                result.append(word)
        return result