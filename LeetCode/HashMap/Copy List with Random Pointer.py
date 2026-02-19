"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        oldnew = {}

        cur = head

        while cur:
            oldnew[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            oldnew[cur].next = oldnew.get(cur.next)
            oldnew[cur].random = oldnew.get(cur.random)
            cur = cur.next

        return oldnew[head]