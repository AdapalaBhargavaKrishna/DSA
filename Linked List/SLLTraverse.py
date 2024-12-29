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

ll = SLL()
ll.head = Node(1)
n2 = Node(2)
n3 = Node(3)

ll.head.next = n2
n2.next = n3

ll.Traverse()