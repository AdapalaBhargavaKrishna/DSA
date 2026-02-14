# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        least = ListNode(0)
        high = ListNode(0)

        less = least
        more = high

        current = head

        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                more.next = current
                more = more.next 
            current = current.next

        more.next = None
        less.next = high.next

        return least.next