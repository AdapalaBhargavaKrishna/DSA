class Solution(object):
    def middleNode(self, head):
        
        temp = head
        index = 1

        while temp.next is not None:
            temp = temp.next
            index += 1
        
        index = (index // 2) + 1

        temp = head
        curindex = 1

        while curindex != index:
            temp = temp.next
            curindex += 1

        return temp

class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.