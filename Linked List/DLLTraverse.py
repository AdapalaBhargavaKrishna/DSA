class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
    
    def ftraverse(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
        print()
    
    def btraverse(self):
        temp = self.head

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end = " ")
            temp = temp.prev
        print()