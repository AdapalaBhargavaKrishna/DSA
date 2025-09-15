class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        newnode = Node(data)
        if self.front is None:
            self.front = self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        pop_data = self.front.data
        self.front = self.front.next
        if self.front is None:  # Queue became empty
            self.rear = None
        print(f"Dequeued {pop_data}")
        return pop_data
        
    def isEmpty(self):
        return self.front is None
    
    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.front.data
    
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            temp = self.front
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")
    
    def size(self):
        count = 0
        temp = self.front
        while temp:
            count += 1
            temp = temp.next
        return count

# Example usage
q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)

q1.display()           # 10 -> 20 -> 30 -> None
print("Size:", q1.size())  # Size: 3

q1.dequeue()           # Dequeued 10
q1.display()           # 20 -> 30 -> None

print("Front element:", q1.peek())  # 20
