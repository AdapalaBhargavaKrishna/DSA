class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        print(f"pushed {data} onto the stack")
    
    def pop(self):
        if not self.isEmpty():
            popped = self.stack.pop()
            print(f"popped {popped} onto the stack")
            return popped
        else:
            print("Stack is Empty")
            return None
        
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            print("Stack is empty")
            return None

    def isEmpty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
print("Top element:", stack.peek())
stack.pop()
stack.display()   