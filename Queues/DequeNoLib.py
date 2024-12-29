class Deque:
    def __init__(self):
        self.queue = []

    def appendLeft(self, data):
        self.queue.insert(0, data)
        print(f"Added {data} to the front")

    def append(self, data):
        self.queue.append(data)
        print(f"Added {data} to the rear")

    def popLeft(self):
        if not self.isEmpty():
            data = self.queue.pop(0)
            print(f"Removed {data} from the front")
            return data
        else:
            print("Deque is empty - cannot remove from the front")
            return None

    def pop(self):
        if not self.isEmpty():
            data = self.queue.pop()
            print(f"Removed {data} from the front")
            return data
        else:
            print("Deque is empty - cannot remove from the front")
            return None
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def front(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            print("Deque is empty - no front element")
            return None
        
    def rear(self):
        if not self.isEmpty():
            return self.queue[-1]
        else:
            print("Deque is empty - no front element")
            return None
    
    def display(self):
        if self.isEmpty():
            print("Deque is Empty")
        else:
            print("Deque elements : ", self.queue)

dq = Deque()

dq.append(10)
dq.append(20)
dq.appendLeft(30)
dq.appendLeft(40)
dq.display()

print("Front element:", dq.front())
print("Rear element:", dq.rear())

dq.popLeft()
dq.pop()
dq.display()

dq.popLeft()
dq.popLeft()
dq.popLeft() 