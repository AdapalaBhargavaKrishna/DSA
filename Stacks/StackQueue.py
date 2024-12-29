class Stack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, data):
        self.queue1.append(data)

    def pop(self):
        if not self.queue1:
            return "Stack Empty"
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

        popped_element = self.queue1.pop(0)

        self.queue1 , self.queue2 = self.queue2 , self.queue1

        return popped_element
    
    def isEmpty(self):
        return len(self.queue1) == 0
    
    def peek(self):
        if not self.queue1:
            return "Stack is Empty"
        
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        
        top = self.queue1.pop(0)

        self.queue2.append(top)

        self.queue1 , self.queue2 = self.queue2 , self.queue1

        return top
    
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top of the stack:", stack.peek())  # Output: 30
print("Popped element:", stack.pop())    # Output: 30
print("Popped element:", stack.pop())    # Output: 20
print("Is stack empty?", stack.isEmpty())  # Output: False
print("Popped element:", stack.pop())    # Output: 10
print("Is stack empty?", stack.isEmpty())  # Output: True