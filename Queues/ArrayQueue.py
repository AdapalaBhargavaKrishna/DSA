class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.front = 0
        self.rear = 0

    def Enqueue(self, data):
        if self.capacity == self.rear :
            print("Queue is Full")
            return
        self.queue.append(data)
        self.rear += 1

    def Dequeue(self):
        if self.front == self.rear :
            print("Queue is Empty")
            return
        x = self.queue.pop(0)
        self.rear -= 1
        print(f"Dequeued {x}")
    
    def queueDisplay(self):
        if self.front == self.rear:
            print("Queue is Empty")
        else:
            print("Queue Elements")
            for i in self.queue:
                print(f"{i} <--", end = " ")
            print()

    def queueFront(self):
        if self.front == self.rear:
            print("Queue is Empty")
        else:
            print(f"Front element is :", self.queue[self.front])

q = Queue(4)
q.queueDisplay()

q.Enqueue(20)
q.Enqueue(30)
q.Enqueue(40)
q.Enqueue(50)

q.queueDisplay()

q.Enqueue(60)

q.queueDisplay()

q.Dequeue()
q.Dequeue()

print("\nAfter two node deletions:")
q.queueDisplay()

q.queueFront()