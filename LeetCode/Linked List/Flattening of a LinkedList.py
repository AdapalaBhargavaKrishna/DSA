# Definiton of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None, child=None):
#         self.val = val
#         self.next = next
#         self.child = child

class Solution:
    def flattenLinkedList(self, head):
        arr=[]
        t1=head
        while t1:
            t2=t1
            while t2:
                arr.append(t2.val)
                t2=t2.child
            t1=t1.next

        arr.sort()

        return self.convert(arr)

    def convert(self,arr):
        if len(arr)==0:
            return None

        head=ListNode(arr[0])
        temp=head
        for i in range(1,len(arr)):
            new_Node=ListNode(arr[i])
            temp.child=new_Node
            temp=temp.child

        return head

# -------------------- NODE DEFINITION --------------------
class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

# -------------------- MULTILEVEL LINKED LIST --------------------
class LinkedList:
    def __init__(self):
        self.head = None

    def display_child_list(self, head):
        """Display nodes using child pointers (flattened list)"""
        elems = []
        curr = head
        while curr:
            elems.append(curr.val)
            curr = curr.child
        print(elems)

# -------------------- SOLUTION --------------------
class Solution:
    def flattenLinkedList(self, head):
        arr = []
        t1 = head
        while t1:
            t2 = t1
            while t2:
                arr.append(t2.val)
                t2 = t2.child
            t1 = t1.next

        arr.sort()
        return self.convert(arr)

    def convert(self, arr):
        if not arr:
            return None

        head = ListNode(arr[0])
        temp = head
        for val in arr[1:]:
            new_node = ListNode(val)
            temp.child = new_node
            temp = temp.child
        return head

# -------------------- TEST --------------------
# Level 1 nodes
n1 = ListNode(5)
n2 = ListNode(10)
n3 = ListNode(19)
n4 = ListNode(28)

# Linking next pointers
n1.next = n2
n2.next = n3
n3.next = n4

# Linking child pointers
n1.child = ListNode(7)
n1.child.child = ListNode(8)
n1.child.child.child = ListNode(30)

n2.child = ListNode(20)

n3.child = ListNode(22)
n3.child.child = ListNode(50)

n4.child = ListNode(35)
n4.child.child = ListNode(40)
n4.child.child.child = ListNode(45)

# Flatten
ll = LinkedList()
sol = Solution()
flat_head = sol.flattenLinkedList(n1)

# Display flattened list
print("Flattened sorted linked list:")
ll.display_child_list(flat_head)
