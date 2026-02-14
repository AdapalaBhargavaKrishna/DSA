# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        max_sum = 0
        slow , fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev , cur = None, slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        while prev:
            if (prev.val + head.val) > max_sum:
                max_sum = prev.val + head.val
            prev, head = prev.next, head.next

        return max_sum

# Example 1:
# Input: head = [5,4,2,1]
# Output: 6
# Explanation: The pair (5, 1) has the maximum sum of 6.

# Example 2:
# Input: head = [4,2,2,3]
# Output: 7
# Explanation: The pair (4, 3) has the maximum sum of 7.