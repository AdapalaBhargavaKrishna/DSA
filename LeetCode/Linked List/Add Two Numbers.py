# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        res = dummy

        total = carry = 0

        while l1 or l2 or carry:
            total = carry
            
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next
        
        return res.next
    
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Node class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# LinkedList helper class to create and display lists
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
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        elems = []
        while current:
            elems.append(current.val)
            current = current.next
        print(elems)

# Solution class
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        res = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carry = total // 10
            dummy.next = ListNode(total % 10)
            dummy = dummy.next

        return res.next

# --- Example usage ---
# Example 1
l1 = LinkedList([2,4,3])
l2 = LinkedList([5,6,4])
sol = Solution()
result_head = sol.addTwoNumbers(l1.head, l2.head)

# Display result
result_list = LinkedList()
result_list.head = result_head
print("Example 1 result:")
result_list.display()  # Output: [7,0,8]

# Example 2
l3 = LinkedList([0])
l4 = LinkedList([0])
result_head2 = sol.addTwoNumbers(l3.head, l4.head)
result_list2 = LinkedList()
result_list2.head = result_head2
print("Example 2 result:")
result_list2.display()  # Output: [0]
