class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

# Example 1:
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

# Example 2:
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.nodes = []  # store references to nodes
        if values:
            for val in values:
                self.insert(val)

    def insert(self, val):
        new_node = ListNode(val)
        self.nodes.append(new_node)
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

def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next

ll = LinkedList([4,5,1,9])
print("Original list:")
ll.display()

# Delete 5 (second node)
curr = ll.head.next
delete_node(curr)
print("After deleting 5:")
ll.display()  # [4,1,9]

# Delete 1 (now second node)
curr = ll.head.next
delete_node(curr)
print("After deleting 1:")
ll.display()  # [4,9]
