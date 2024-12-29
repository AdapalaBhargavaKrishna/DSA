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
            print(temp.data)
            temp = temp.next
        print()

    def Insertatbeg(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def Insertatend(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newnode

    def Insertatpos(self, data, pos):
        newnode = Node(data)
        if not self.head:
            if pos == 0:
                self.head = newnode
            else:
                print("position out of bounds")
            return
        
        if pos == 0:
            newnode.next = self.head
            self.head = newnode
            return

        temp = self.head
        c = 0
        while temp and c < pos - 1:
            temp = temp.next
            c += 1

        if temp is None:
            print("position out of bounds")
        else:    
            newnode.next = temp.next
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

ll.Insertatbeg(1)  # List: 1
ll.Insertatend(2)  # List: 1 -> 2
ll.Insertatpos(3, 1)  # List: 1 -> 3 -> 2
ll.Deleteatbeg()  # List after deletion: 3 -> 2
ll.Deleteatend()  # List after deletion: 3
ll.Deleteatpos(1) # Output: Position out of bounds
ll.Traverse()  # Output: 3
