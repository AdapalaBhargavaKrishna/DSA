# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        length = 0
        result = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1

        temp = head
        for i in range(length - 1, -1, -1):
            result += temp.val * (2**i)
            temp = temp.next
        
        return result