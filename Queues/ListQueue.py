class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        print(f"Enqueued {data} to the  Queue") 

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty. Cannot Dequeue")
            return None
        data = self.queue.pop(0)
        print(f"Dequeued {data} from the Queue")
        return data
    
    def front(self):
        if self.isEmpty():
            print("Queue is Empty")
            return None
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Queue: ", self.queue)

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print("Front element:", q.front())
q.dequeue()
q.display()
print("Queue size:", q.size())
q.dequeue()
q.dequeue()
q.dequeue() 