"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        if not head:
            return head

        stack = [head]
        prev = None   

        while stack:
            cur = stack.pop()

            if prev:
                prev.next = cur
                cur.prev = prev

            if cur.next:
                stack.append(cur.next)

            if cur.child:
                stack.append(cur.child)
                cur.child = None
            prev = cur
        return head
