class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    
    def Traverse(self):
        if not self.head:
            print("List is Empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print()

    def Insert(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newnode

    def Deleteatbeg(self):
        if self.head is None:
            print("List is Empty")
            return
        self.head = self.head.next

    def Deleteatend(self):
        if self.head is None:
            print("List is Empty")
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        temp = self.head
        while temp.next and temp.next.next:
            temp = temp.next
        temp.next = None

    def Deleteatpos(self, pos):
        if not self.head:
            print("List is Empty")
            return
        if pos == 0:
            self.head = self.head.next
            return

        temp = self.head
        c = 0

        while temp.next and c < pos - 1:
            temp = temp.next
            c += 1

        if temp.next is None:
            print("Position out of bounds")
        else:
            temp.next = temp.next.next

ll = SLL()

ll.Insert(1)  # List: 1
ll.Insert(2)  # List: 1 -> 2
ll.Insert(3)  # List: 1 -> 2 -> 3
ll.Insert(4)  # List: 1 -> 2 -> 3 -> 4
ll.Traverse()  # Output: 1 -> 2 -> 3 -> 4 -> None
ll.Deleteatbeg()  # List after deletion: 2 -> 3 -> 4
ll.Traverse()
ll.Deleteatend()  # List after deletion: 2 -> 3
ll.Traverse()
ll.Deleteatpos(1)  # List after deletion: 2
ll.Traverse()
ll.Deleteatpos(10)  # Output: Position out of bounds
ll.Traverse()