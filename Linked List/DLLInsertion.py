class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
    
    def insertatbeg(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        
    def insertatend(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = newnode
            newnode.prev = temp

    def insertatpos(self, data, pos):
        newnode = Node(data)
        if self.head is None:
            if pos == 0:
                self.head = newnode
            else:
                print("Invalid position")
            return
        if pos == 0:
            self.insertatbeg(data)
        
        temp = self.head
        c = 0

        while temp and c < pos - 1:
            temp = temp.next
            c += 1

        temp .next = newnode
        newnode.prev = temp