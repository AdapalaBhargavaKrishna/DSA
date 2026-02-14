# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow , fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev , cur = None, slow

        while cur:
            nxt = cur.next
            cur.next =  prev 
            prev = cur
            cur = nxt

        while prev:
            if prev.val != head.val:
                return False
            prev, head = prev.next, head.next
        return True

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false