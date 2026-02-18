import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        if lists == [] or lists == [[]]:
            return None
        heap = []

        for i , node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        cur = dummy
        while heap:
            val, i, node = heapq.heappop(heap)

            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(heap, (node.next.val,i, node.next))

        return dummy.next