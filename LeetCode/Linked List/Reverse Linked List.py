
def reverseList(self, head):

    prev = None
    current = head
    while current:
        nextnode = current.next
        current.next = prev
        prev = current
        current = nextnode
        
    return prev
    
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

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
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        elems = []
        while current:
            elems.append(current.data)
            current = current.next
        print(elems)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode
        self.head = prev

# --- Example usage ---
ll = LinkedList()

# Example 1: head = [1,2,3,4,5]
for i in [1, 2, 3, 4, 5]:
    ll.insert(i)

print("Original list:")
ll.display()

ll.reverse()
print("Reversed list:")
ll.display()

# Example 2: head = [1,2]
ll2 = LinkedList()
for i in [1, 2]:
    ll2.insert(i)

print("Original list 2:")
ll2.display()

ll2.reverse()
print("Reversed list 2:")
ll2.display()