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
        if self.front is None:
            print("list is empty")
        pop_data = self.front.data
        self.front = self.front.next
        print(f"popped {pop_data} from queue")
        
    def is_empty(self):
        return self.rear is None
    
    def peek(self):
        return self.rear.data
    
    def display(self):
        if self.front is None:
            print("list is empty")

        else:
            temp = self.front
            while temp is not None:
                print(temp.data)
                temp = temp.next
    
    def size(self):
        if self.front is None:
            return 0
        else:
            temp = self.front
            size = 0
            while temp is not None:
                size += 1
                temp = temp.next
            return f"size : {size}"

q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)

q1.display()

print(q1.size())
q1.dequeue()
q1.display()