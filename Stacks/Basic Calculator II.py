class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        prev_op = '+'
        s += '+'

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == ' ':
                continue

            else:
                if prev_op == '+':
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack.append(stack.pop() * num)
                elif prev_op == '/':
                    top = stack.pop()
                    stack.append(int(top / num))

                prev_op = ch
                num = 0

        return sum(stack)