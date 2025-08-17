class Solution(object):
    def reverseList(self, head):

        prev = None
        current = head
        while current:
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode
            
        return prev
    
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]