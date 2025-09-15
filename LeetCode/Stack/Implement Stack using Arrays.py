class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x):
        self.stack.append(x)
        self.size += 1
        return None

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow! Cannot pop")
            return None
        self.size -= 1
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.stack[self.size - 1]

    def isEmpty(self):
        return self.size == 0

    def display(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Stack (bottom → top):", self.stack[:self.size])


# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
print("Top element:", stack.peek())
stack.pop()
stack.display()   