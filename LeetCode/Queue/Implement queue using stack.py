class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def _shift_stacks(self):
        if not self.stack2:  # Only shift if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        self._shift_stacks()
        if not self.stack2:
            return "Queue is Empty"
        return self.stack2.pop()

    def front(self):
        self._shift_stacks()
        if not self.stack2:
            return "Queue is Empty"
        return self.stack2[-1]

    def isEmpty(self):
        return not self.stack1 and not self.stack2
    
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front of the queue:", queue.front())  # Output: 10
print("Dequeued element:", queue.dequeue())  # Output: 10
print("Dequeued element:", queue.dequeue())  # Output: 20
print("Is queue empty?", queue.isEmpty())    # Output: False
print("Dequeued element:", queue.dequeue())  # Output: 30
print("Is queue empty?", queue.isEmpty())    # Output: True

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        if not self.stack2:       # shift only if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return "Queue is Empty"
        return self.stack2.pop()

    def front(self):
        if not self.stack2:       # shift only if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return "Queue is Empty"
        return self.stack2[-1]

    def isEmpty(self):
        return not self.stack1 and not self.stack2
    

# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front of the queue:", queue.front())  # Output: 10
print("Dequeued element:", queue.dequeue())  # Output: 10
print("Dequeued element:", queue.dequeue())  # Output: 20
print("Is queue empty?", queue.isEmpty())    # Output: False
print("Dequeued element:", queue.dequeue())  # Output: 30
print("Is queue empty?", queue.isEmpty())    # Output: True
