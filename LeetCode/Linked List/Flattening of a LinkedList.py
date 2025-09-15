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
