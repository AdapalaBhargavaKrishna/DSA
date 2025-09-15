class MinStack():

    def __init__(self):
        self.stack=[]


    def push(self, val):
        if self.isEmpty():
            self.stack.append((val,val))
        else:
            self.stack.append((val,min(val,self.stack[-1][1])))

    def pop(self):
        return self.stack.pop()[0]

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]

    def isEmpty(self):
        return len(self.stack)==0

    def display(self):
      print("current stack:")
      for i in self.stack:
        print(i[0],end = "  ")
      print()


s1=MinStack()
s1.push(12)
s1.push(15)
s1.push(10)
print(s1.getMin())
print(s1.pop())
print(s1.getMin())
s1.display()
