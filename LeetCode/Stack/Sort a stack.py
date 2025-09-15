class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.isEmpty():
            return None

        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)


def sortStack(stack):
  tempStack=Stack()

  while not stack.isEmpty():
    curr=stack.pop()

    while not tempStack.isEmpty() and tempStack.peek()<curr:
      stack.push(tempStack.pop())

    tempStack.push(curr)

  while not tempStack.isEmpty():
    stack.push(tempStack.pop())


s1=Stack()
s1.push(15)
s1.push(3)
s1.push(12)
s1.push(5)
s1.display()
s2=sortStack(s1)
s1.display()
