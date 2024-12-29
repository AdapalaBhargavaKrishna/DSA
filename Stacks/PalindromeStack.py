class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None

    def isEmpty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)

def isPalindrome(Inputstr):
    stack = Stack()
    mid = len(Inputstr)//2
    
    for i in range(mid, len(Inputstr)):
        stack.push(Inputstr[i])

    for i in range(mid):
        if Inputstr[i] != stack.pop():
            return False
    return True

print(isPalindrome("masddtam"))  # False
print(isPalindrome("madam"))     # True
print(isPalindrome("maddam"))    # True
print(isPalindrome("madtam"))    # False