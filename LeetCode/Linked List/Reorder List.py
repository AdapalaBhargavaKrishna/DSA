# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return

        slow , fast = head , head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev, cur = None, slow.next
        slow.next = None
        
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        first, second = head, prev
        while second:
            tp1 = first.next
            tp2 = second.next

            first.next = second
            second.next = tp1

            first = tp1
            second = tp2