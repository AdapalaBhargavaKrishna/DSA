class Solution(object):
    def backspaceCompare(self, s, t):

        def bc(st):
            result = []
            for ch in st:
                if ch == '#':
                    if result:
                        result.pop()
                    else:
                        result.append(ch)
            return "".join(result)
        
        return bc(s) == bc(t)

# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

# Example 2:
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".