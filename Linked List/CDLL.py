class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class CDLL:
    def __init__(self):
        self.head = None
    
    def insertatbeg(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            self.head.next=self.head
            self.head.prev=self.head

        else:
            newnode.next = self.head
            newnode.prev = self.head.prev
            self.head.prev.next = newnode
            self.head.prev = newnode
            self.head = newnode
        
    def insertatend(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            self.head.next = self.head
            self.head.prev = self.head
        
        else:
            newnode.prev = self.head.prev
            newnode.next = self.head
            self.head.prev.next = newnode
            self.head.prev = newnode

    def insertatpos(self, data, pos):
        print(f"\ninserting {data} at the pos: {pos}")
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            self.head.next = self.head
            self.head.prev = self.head
        else:
            if pos == 1:
                self.inseratbeg(data)
            else:
                c = 1
                temp = self.head
                while c < pos - 1:
                    temp = temp.next
                    c += 1
                
                newnode.next = temp.next
                newnode.prev = temp
                temp.next.prev = newnode
                temp.next = newnode

    def delatbeg(self):
        if self.head is None:
            print("List is empty")
        else:
            print(f"\ndeleting {self.head.data} at begining")
            self.head.prev.next = self.head.next
            self.head.next.prev = self.head.prev
            self.head = self.head.next
    
    def delatend(self):
        if self.head is None:
            print("List is empty")
        else:
            print(f"\ndeleting {self.head.prev.data} at end")
            self.head.prev.prev.next = self.head
            self.head.prev = self.head.prev.prev

    def delatpos(self, pos):
        if self.head is None:
            print("List is empty")
        else:
            if pos == 1:
                self.delatbeg()
            else:
                c = 1 
                temp = self.head
                while c < pos:
                    temp = temp.next
                    c += 1
                print(f"\ndeleting  {temp.data} at pos {pos}")
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
            
    def ftraverse(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while True:
                print(temp.data)
                temp = temp.next
                if temp is self.head:
                    break

cdll = CDLL()
cdll.insertatbeg(10)
cdll.insertatbeg(20)
cdll.ftraverse()

cdll.insertatend(30)
cdll.insertatend(40)
cdll.ftraverse()

cdll.delatbeg()
cdll.ftraverse()

cdll.delatend()
cdll.ftraverse()

cdll.insertatpos(3,40)
cdll.ftraverse()

cdll.insertatend(50)
cdll.insertatend(60)
cdll.ftraverse()


cdll.delatpos(4)
cdll.ftraverse()