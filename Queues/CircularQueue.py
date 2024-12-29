class CircularQueue:
    def __init__(self, maxsize):
        self.queue = list()
        self.maxsize = maxsize
        self.front = 0
        self.rear = 0

    def enqueue(self, data):
        if (self.size() == self.maxsize - 1):
            return "Queue is Full"
        else:
            self.queue.append(data)
            self.rear = (self.rear + 1) % self.maxsize
            return True
        
    def dequeue(self):
        if self.size() == 0:
            return "Queue is Empty"
        else:
            data = self.queue[self.front]
            self.front = (self.front + 1) % self.maxsize
            return data
        
    def size(self):
        if self.rear >= self.front:
            qsize = self.rear - self.front
        else:
            qsize = self.maxsize - (self.front - self.rear)
        return qsize
    
size = input("Enter the size of the Circular Queue: ")  # Input for queue size
q = CircularQueue(int(size))  # Create a Circular Queue with the given size

# Enqueue operations
print(q.enqueue(10))  # Enqueue 10
print(q.enqueue(20))  # Enqueue 20
print(q.enqueue(30))  # Enqueue 30
print(q.enqueue(70))  # Enqueue 70

print(q.enqueue(80))  # Should return "Queue is full!"

print(q.dequeue())  # Dequeue the first element (10)
print(q.dequeue())  # Dequeue the second element (20)
print(q.dequeue())  # Dequeue the third element (30)
print(q.dequeue())  # Dequeue the fourth element (70)

print(q.size())  # Should return 0 as the queue is empty