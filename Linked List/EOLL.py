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

    def seperate(self):
        if self.head is None:
            print("list is empty")

        else:
            even_end = even_start = None
            odd_end = odd_start = None

            current = self.head

            while current:

                if current.data % 2 == 0:
                    if even_start is None:
                        even_start = even_end = current
                    else:
                        even_end.next = current
                        even_end = current

                else:
                    if odd_start is None:
                        odd_start = odd_end = current
                    else:
                        odd_end.next = current
                        odd_end = current
                current = current.next

            if even_end:
                even_end.next = odd_start
                self.head = even_start
            else:
                self.head = odd_start

            if odd_end:
                odd_end.next = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.insert(8)
ll.insert(9)
ll.insert(10)
ll.insert(11)
ll.insert(12)
ll.insert(13)

print("Original List:")
ll.display()

ll.seperate()
print("List after separating even and odd numbers:")
ll.display()