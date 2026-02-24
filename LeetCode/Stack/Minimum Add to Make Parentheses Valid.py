class Solution(object):
    def minAddToMakeValid(self, s):
        stack = []
        need = 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    need += 1

        return need + len(stack)