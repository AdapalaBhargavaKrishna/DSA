class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        current = head
        size = 0

        while current:
            size += 1
            current = current.next


        x = size - n
        current = dummy
        for _ in range(x):
            current = current.next

        current.next = current.next.next

        return dummy.next
    
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# -------------------- SINGLY LINKED LIST --------------------
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

# -------------------- SOLUTION --------------------
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        current = head
        size = 0

        # Calculate length
        while current:
            size += 1
            current = current.next

        # Find node before the one to remove
        x = size - n
        current = dummy
        for _ in range(x):
            current = current.next

        # Remove the node
        if current.next:
            current.next = current.next.next

        return dummy.next

# -------------------- TEST --------------------
sol = Solution()

# Example 1
ll1 = LinkedList([1,2,3,4,5])
print("Original list 1:")
ll1.display()
ll1.head = sol.removeNthFromEnd(ll1.head, 2)
print("After removing 2nd from end:")
ll1.display()  # Output: [1,2,3,5]

# Example 2
ll2 = LinkedList([1])
print("Original list 2:")
ll2.display()
ll2.head = sol.removeNthFromEnd(ll2.head, 1)
print("After removing 1st from end:")
ll2.display()  # Output: []
