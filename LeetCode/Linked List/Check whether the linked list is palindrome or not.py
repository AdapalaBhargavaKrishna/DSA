class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def display(self):
        elems = []
        curr = self.head
        while curr:
            elems.append(curr.data)
            curr = curr.next
        print("SLL:", elems)

    def is_palindrome(self):
        
        elems = []
        curr = self.head
        while curr:
            elems.append(curr.data)
            curr = curr.next
        return elems == elems[::-1]

# Example 1: Palindrome list
sll1 = SinglyLinkedList()
for i in [1,2,3,2,1]:
    sll1.insert(i)
sll1.display()
print("Is palindrome?", sll1.is_palindrome())  # True

# Example 2: Non-palindrome list
sll2 = SinglyLinkedList()
for i in [1,2,3,4]:
    sll2.insert(i)
sll2.display()
print("Is palindrome?", sll2.is_palindrome())  # False
