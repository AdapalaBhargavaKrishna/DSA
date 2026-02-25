class Solution(object):
    def minRemoveToMakeValid(self, s):
        stack = []
        extra = set()
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    extra.add(i)
        res = []
        for i , c in enumerate(s):
            if i not in extra and i not in stack:
                res.append(c)
        return ''.join(res)