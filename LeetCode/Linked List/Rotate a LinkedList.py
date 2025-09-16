class Solution(object):
    def rotateRight(self, head, k):
        
        if not head or not head.next or k == 0:
            return head

        length = 1
        current = head

        while current.next:
            current = current.next
            length += 1

        current.next = head

        k  = k % length
        steps_to_new_head = length - k
        new_tail = head

        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
    
# -------------------- NODE & LINKED LIST --------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        if values:
            for val in values:
                self.insert(val)

    def insert(self, val):
        new_node = ListNode(val)
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
            elems.append(curr.val)
            curr = curr.next
        print(elems)

def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head

    # Compute length
    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1

    # Make it circular
    current.next = head

    # Find new head
    k = k % length
    steps_to_new_head = length - k
    new_tail = head
    for _ in range(steps_to_new_head - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head

ll = LinkedList([1,2,3,4,5])
print("Original list:")
ll.display()

# Rotate by k = 2
ll.head = rotateRight(ll.head, 2)
print("After rotating by 2:")
ll.display()  # Output: [4,5,1,2,3]

# Another test: rotate by k = 8
ll.head = rotateRight(ll.head, 8)
print("After rotating by 8:")
ll.display()  # Output: [2,3,4,5,1]
