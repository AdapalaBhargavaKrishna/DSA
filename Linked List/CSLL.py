class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CSLL:
    def __init__(self):
        self.head = None
    
    def insertatbeg(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            self.head.next = self.head
        
        else:
            tempnode = self.head
            while tempnode.next != self.head:
                tempnode = tempnode.next
            
            print(f"inserting {newnode.data} at the beginning")
            newnode.next = self.head
            tempnode.next = newnode
            self.head = newnode
    
    def insertatend(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            self.head.next = self.head
        else:
            tempnode = self.head
            while tempnode.next is not self.head:
                tempnode = tempnode.next

            print(f"\n inserting {newnode.data} at the end")
            tempnode.next = newnode
            newnode.next = self.head

    def insertatpos(self, pos, data):
        newnode = Node(data)
        if self.head is None:
            if pos == 1:
                self.head = newnode
                self.head.next = self.head
                print(f"\ninserting {newnode.data} at pos {pos}")
            else:
                print("position out of bounds")
            return
            
        if pos == 1:
            tempnode = self.head
            while tempnode.next != self.head:
                tempnode = tempnode.next

            newnode.next = self.head
            tempnode.next = newnode
            self.head = newnode
        
        else:
            print("\n inserting at position", pos)
            tempnode = self.head
            c = 1

            while c < pos - 1 and tempnode.next != self.head:
                tempnode = tempnode.next
                c += 1
            
            if c < pos - 1:
                print("Position out of bounds")
                return
            
            newnode.next = tempnode.next
            tempnode.next = newnode

    def delatbeg(self):
        if self.head is None:
            print("list is empty")
        else:
            print(f"\nDeleting {self.head.data} from the beginning")
            if self.head.next==self.head:
                self.head=None
            else:
                tempnode = self.head
                while tempnode.next != self.head:
                    tempnode = tempnode.next
                self.head = self.head.next
                tempnode.next = self.head

    def delatend(self):
        if self.head is None:
            print("list is empty")
        else:
            if self.head.next==self.head:
                self.head = None
            else:
                temp2 = self.head
                temp1 = None

                while temp2.next != self.head:
                    temp1 = temp2
                    temp2 = temp2.next

                temp1.next = temp2.next
                temp2.next = None

    def delatpos(self, pos):
        if self.head is None:
            print("list is empty")
        else:
            if self.head.next == self.head:
                self.head = None

            elif pos == 1:
                self.head = self.head.next
                tempnode = self.head
                while tempnode.next != self.head:
                    tempnode = tempnode.next
                tempnode.next = self.head
            
            else:
                temp1 = None
                temp2 = self.head
                c = 1
                
                while c < pos:
                    temp1 = temp2
                    temp2 = temp2.next
                    c += 1
                
                if temp2 is None:
                    print(f"{pos} out of bounds")
                
                print(f"deleted node at pos {pos}")
                temp1.next = temp2.next
                temp2.next = None

    def ftraverse(self):
        print("\nforward traverse")
        if self.head is None:
            print("list is empty")
        else:
            temp_node=self.head
            while True:
                print(temp_node.data)
                temp_node=temp_node.next

                if temp_node == self.head:
                    break



scll=CSLL()
scll.insertatbeg(10)
scll.insertatbeg(5)
scll.insertatend(15)
scll.ftraverse()

scll.insertatpos(1,12)
scll.ftraverse()

scll.delatbeg()
scll.ftraverse()

scll.delatend()
scll.ftraverse()

scll.insertatbeg(20)
scll.insertatend(30)
scll.ftraverse()

scll.delatpos(3)
scll.ftraverse()
