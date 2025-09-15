class Queue:
    def __init__(self, c):
        self.queue = []
        self.front = self.rear = 0
        self.capacity = c

    def Enqueue(self, data):
        if self.rear == self.capacity:
            print("\nQueue is full")
        else:
            self.queue.append(data)
            self.rear += 1
            print(f"Enqueued {data}")

    def Dequeue(self):
        if self.front == self.rear:
            print("Queue is empty")
            return None
        x = self.queue.pop(0)
        self.front += 1
        print(f"Dequeued {x}")
        return x

    def queueDisplay(self):
        if self.front == self.rear:
            print("\nQueue is Empty")
            return
        print("Queue Elements:", end=" ")
        for i in self.queue:
            print(i, "<--", end=" ")
        print()

    def isEmpty(self):
        return self.front == self.rear

    def queueFront(self):
        if self.front == self.rear:
            print("\nQueue is Empty")
            return
        print("\nFront Element is:", self.queue[0])
        
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

print("\nAfter two node deletions\n")
q.queueDisplay()
q.queueFront()
