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



class SortedStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack or x >= self.stack[-1]:
            self.stack.append(x)
        else:
            temp = self.stack.pop()
            self.push(x)
            self.stack.append(temp)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()

    def top(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack (bottom → top):", self.stack)


# Example usage
s = SortedStack()
s.push(30)
s.display()
s.push(-5)
s.display()
s.push(18)
s.display()
s.push(14)
s.push(-3)
s.display()