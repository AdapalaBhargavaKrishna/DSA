#Write a python program to rotate a linked list.
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

    def reverse(self):
      if self.head is None:
        print("list is empty")
      else:
        back=None
        front=self.head
        while front is not None:
          next_node=front.next
          front.next=back
          back=front
          front=next_node

        self.head=back

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)

print("Original List:")
ll.display()

print("\nreversed list")
ll.reverse()
ll.display()