class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LL:
    def __init__(self):
        self.head=None
            
    def insertatbeg(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp_node=self.head
            while temp_node is not None:
                print(temp_node.data , end =" ")
                temp_node=temp_node.next

    def middle(self):
        if self.head is None:
            print("List is empty")
            return None
        tempf = self.head
        temps = self.head

        while tempf and tempf.next:
            tempf = tempf.next.next
            temps = temps.next
        
        print(f"\nThe middle element is : {temps.data}")
    

ll=LL()

ll.insertatbeg(30)
ll.insertatbeg(20)
ll.insertatbeg(10)

ll.display()

ll.middle()