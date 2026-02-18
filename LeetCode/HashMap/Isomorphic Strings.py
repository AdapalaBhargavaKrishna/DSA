class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        hs = {}
        ht = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            if a in hs and hs[a] != b:
                return False
            if b in ht and ht[b] != a:
                return False

            hs[a] = b
            ht[b] = a

        return True