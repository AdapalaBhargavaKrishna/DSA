class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        newnode = Node(data)
        newnode.next = self.top
        self.top = newnode
        print(f"pushed {data} onto the stack")
    
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty cannnot pop")
            return None
        popped = self.top.data
        self.top = self.top.next
        print(f"popped {popped} from the stack")
        return popped
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty!")
            return None
        return self.top.data
    
    def isEmpty(self):
        return self.top is None
    
    def display(self):
        if self.isEmpty():
            print("Stack isEmpty")
        else:
            temp = self.top
            while temp:
                print(temp.data, end = " ")
                temp = temp.next
            print()
    
    def size(self):
        count = 0 
        temp = self.top 
        while temp:
            count += 1
            temp = temp.next
        return count
    

s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.display()
print(f"Stack size: {s1.size()}")
s1.pop()
s1.display()
print(f"Top element: {s1.peek()}")
s1.pop()
s1.pop()
s1.pop()