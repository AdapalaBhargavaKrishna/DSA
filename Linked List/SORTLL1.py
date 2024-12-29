class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newnode = Node(data)

        if self.head is None or self.head.data >= newnode.data:
            newnode.next = self.head
            self.head = newnode

        else:
            temp = self.head
            while temp.next and temp.next.data < newnode.data:
                temp = temp.next
            
            newnode.next = temp.next
            temp.next = newnode

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


ll = LinkedList()
ll.insert(5)
ll.insert(1)
ll.insert(4)
ll.insert(2)
ll.insert(3)
print("Sorted Linked List:")
ll.display()