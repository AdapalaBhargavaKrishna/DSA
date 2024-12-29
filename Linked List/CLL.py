class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
 
    def insert(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newnode

    def  create_cycle(self, pos):
        if self.head is None:
            return
        cycle_node = None
        temp = self.head
        count = 1
        while temp.next is not None:
            if count == pos:
                cycle_node = temp
            temp = temp.next
            count += 1
        if cycle_node:
            temp.next = cycle_node
            
    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                print("Cyle detected in linked list")
                return True
        print("No cycle detected in the linked list.")
        return False
    
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp_node=self.head
            while temp_node is not None:
                print(temp_node.data , end =" ")
                temp_node=temp_node.next
            print()
    
    
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)
ll.display()

ll.head.next.next.next.next=ll.head.next

ll.display()
ll.has_cycle()