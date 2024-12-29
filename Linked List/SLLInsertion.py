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


ll = SLL()

ll.Insertatbeg(1)  # List: 1
ll.Insertatbeg(0)  # List: 0 -> 1
ll.Insertatend(2)  # List: 0 -> 1 -> 2
ll.Insertatend(3)
ll.Insertatpos(1, 0)  # Insert 1 at position 0 
ll.Insertatpos(4, 1)  # Insert 2 at position 1
ll.Insertatpos(5, 1)  # Insert 3 at position 1
ll.Insertatpos(6, 10) # Position out of bounds
ll.Traverse()  # Output: 1 -> 5 -> 4 -> 0 -> 1 -> 2 -> 3 ->