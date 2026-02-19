class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        hs = {}
        hp = {}

        for st , word in zip(pattern, words):
            if st in hs and hs[st] != word:
                return False
            if word in hp and hp[word] != st:
                return False
            
            hs[st] = word
            hp[word] = st
        return True