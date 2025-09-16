class Solution(object):
    def middleNode(self, head):
        
        temp = head
        index = 1

        while temp.next is not None:
            temp = temp.next
            index += 1
        
        index = (index // 2) + 1

        temp = head
        curindex = 1

        while curindex != index:
            temp = temp.next
            curindex += 1

        return temp

class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

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
        curr = self.head
        elems = []
        while curr:
            elems.append(curr.data)
            curr = curr.next
        print("SLL:", elems)

    def middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

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
        curr = self.head
        elems = []
        while curr:
            elems.append(curr.data)
            curr = curr.next
        print("DLL:", elems)

    def middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

# -------------------- CIRCULAR LINKED LIST --------------------
class CLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = CLLNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head

    def display(self):
        elems = []
        if not self.head:
            print("CLL:", elems)
            return
        curr = self.head
        while True:
            elems.append(curr.data)
            curr = curr.next
            if curr == self.head:
                break
        print("CLL:", elems)

    def middle(self):
        if not self.head:
            return None
        slow = self.head
        fast = self.head
        while fast.next != self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next
        return slow.data

# -------------------- TEST --------------------
# SLL Example
sll = SinglyLinkedList()
for i in [1,2,3,4,5]:
    sll.insert(i)
sll.display()
print("Middle of SLL:", sll.middle())

# DLL Example
dll = DoublyLinkedList()
for i in [1,2,3,4,5,6]:
    dll.insert(i)
dll.display()
print("Middle of DLL:", dll.middle())

# CLL Example
cll = CircularLinkedList()
for i in [1,2,3,4,5,6,7]:
    cll.insert(i)
cll.display()
print("Middle of CLL:", cll.middle())
