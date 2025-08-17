class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        current = head
        size = 0

        while current:
            size += 1
            current = current.next


        x = size - n
        current = dummy
        for _ in range(x):
            current = current.next

        current.next = current.next.next

        return dummy.next
    
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []