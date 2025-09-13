class Solution(object):
    def rotateRight(self, head, k):
        
        if not head or not head.next or k == 0:
            return head

        length = 1
        current = head

        while current.next:
            current = current.next
            length += 1

        current.next = head

        k  = k % length
        steps_to_new_head = length - k
        new_tail = head

        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        
        return new_head