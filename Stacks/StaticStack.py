class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * self.size
        self.top = -1

    def isEmpty(self):
        return self.top == -1
    
    def display(self):
        if self.isEmpty():
            print("Stack is is Empty")
            return None
        else:
            print(self.stack[: self.top + 1])

    def push (self, data):
        if self.top == self.size - 1:
            print("Stack is full")
        else:
            self.top += 1
            self.stack[self.top] = data
            print(f"Pushed {data} onto the stack.")

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow! The stack is empty.")
            return None
        else:
            popped = self.stack[self.top]
            self.top -= 1
            print(f"Popped {popped} from the stack.")
            return popped


    def peek(self):
        if self.isEmpty():
            print("Stack is empty.")
            return None
        else:
            return self.stack[self.top]
        
stack = Stack(5) 
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)  
stack.display()
print("Top element:", stack.peek())
stack.pop()
stack.display()