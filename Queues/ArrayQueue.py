class Queue:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def Enqueue(self, x):
        if self.size == self.capacity:
            print("Queue is Full")
            return None
        self.queue[self.rear] = x
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def Dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        x = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return x

    def getFront(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        return self.queue[self.front]

    def isEmpty(self):
        return self.size == 0

    def queueDisplay(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Queue Elements:", end=" ")
            for i in range(self.size):
                print(self.queue[(self.front + i) % self.capacity], end=" <-- ")
            print()

q = Queue(4)
q.queueDisplay()

q.Enqueue(20)
q.Enqueue(30)
q.Enqueue(40)
q.Enqueue(50)

q.queueDisplay()

q.Enqueue(60)

q.Dequeue()
q.Dequeue()

print("\nAfter two node deletions:")
q.queueDisplay()

print("Front element:", q.getFront())
