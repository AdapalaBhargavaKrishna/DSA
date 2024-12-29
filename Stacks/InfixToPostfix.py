class Stack:
    def __init__(self):
        self.stack = []  

    def push(self, item):
        self.stack.append(item)  

    def pop(self):
        return self.stack.pop()  

    def isEmpty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1] 
    
    def __str__(self):
        return str(self.stack)
    
def infixtopostfix(expression):
    precedence = {}
    precedence["*"] = 3
    precedence["/"] = 3
    precedence["+"] = 2
    precedence["-"] = 2
    precedence["("] = 1

    operator_stack = Stack()
    postfix_evaluation = []

    tokens = expression.split()

    for token in tokens:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "1234567890":
            postfix_evaluation.append(token)
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            top_operator = operator_stack.pop()
            while top_operator != '(':
                postfix_evaluation.append(top_operator)
                top_operator = operator_stack.pop()
        else:
            while (not operator_stack.isEmpty()) and (precedence[operator_stack.peek()] >= precedence[token]):
                postfix_evaluation.append(operator_stack.pop())
            operator_stack.push(token)
        
    while not operator_stack.isEmpty():
        postfix_evaluation.append(operator_stack.pop())

    return " ".join(postfix_evaluation)


print(infixtopostfix("A + B * C + D"))
print(infixtopostfix("( A + B ) * C - ( D - E ) * ( F + G )"))