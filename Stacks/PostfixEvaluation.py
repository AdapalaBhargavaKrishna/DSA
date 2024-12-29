class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return self.stack == []
    
    def peek(self):
        return self.stack[-1]
    
    def __str__(self):
        return str(self.stack)
    
def postfixEval(postfixExpression):
    operandStack = Stack()

    tokens = postfixExpression.split()

    for token in tokens:
        if token.isdigit():
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('1 2 3 * + 5 -'))  # Output: 2