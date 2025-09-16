# -------------------- SINGLY LINKED LIST --------------------
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

    def get_before_after(self, node):
        prev = None
        curr = self.head
        while curr and curr != node:
            prev = curr
            curr = curr.next
        after = curr.next if curr else None
        return (prev, after)

# -------------------- DOUBLY LINKED LIST --------------------
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = DLLNode(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def display(self):
        elems = []
        curr = self.head
        while curr:
            elems.append(curr.data)
            curr = curr.next
        print("DLL:", elems)

    def get_before_after(self, node):
        prev = node.prev
        after = node.next
        return (prev, after)

# -------------------- TEST --------------------
# Singly Linked List Example
sll = SinglyLinkedList()
for i in [10,20,30,40,50]:
    sll.insert(i)
sll.display()

# Pick node with value 30
node = sll.head.next.next
prev_node, next_node = sll.get_before_after(node)
print("SLL Node:", node.data)
print("Before:", prev_node.data if prev_node else None)
print("After:", next_node.data if next_node else None)

# Doubly Linked List Example
dll = DoublyLinkedList()
for i in [100,200,300,400]:
    dll.insert(i)
dll.display()

# Pick node with value 300
node = dll.head.next.next
prev_node, next_node = dll.get_before_after(node)
print("DLL Node:", node.data)
print("Before:", prev_node.data if prev_node else None)
print("After:", next_node.data if next_node else None)
