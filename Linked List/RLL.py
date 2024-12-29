class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def rotate(self):
        
        if self.head is None or self.head.next is None:
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        last = temp
        last2 = self.head
        while last2.next != last:
            last2 = last2.next

        last2.next = None
        last.next =self.head
        self.head = last

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)

print("Original List:")
ll.display()

ll.rotate()
print("List after rotation")
ll.display()