class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def insert(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = newnode
            newnode.prev = temp
    
    def deleteatbeg(self):
        if self.head is None:
            print("List is Empty")
            return
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
    
    def deleteatend(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        if temp.prev is None:
            self.head = None
        else:
            temp.prev.next = None

    def deleteatpos(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos == 0:
            self.deleteatbeg()
            return
    
        temp = self.head
        c = 0

        while temp and c < pos:
            temp = temp.next
            c += 1
        
        if temp is None:
            print("Position out of bounds")
        else:
            if temp.next:
                temp.next.prev = temp.prev
            if temp.prev:
                temp.prev.next = temp.next