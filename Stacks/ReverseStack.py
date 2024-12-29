class Stack:
    def __init__(self):
        self.stack = []

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        if len(self.stack) == 0:
            print("empty")
        else:
            return self.stack.pop()

def reverse_string(string):
    s1 = Stack()

    for char in string:
        s1.push(char)

    reversed_str = ""
    while len(s1.stack) != 0:
        reversed_str += s1.pop()

    return reversed_str

def reverse_array(arr):
    s1 = Stack()

    for element in arr:
        s1.push(element)

    reversed_arr = []
    while len(s1.stack) != 0:
        reversed_arr.append(s1.pop())

    return reversed_arr

string = "Bhargava"
reversed_string = reverse_string(string)
print("Reversed string:", reversed_string)

arr = [1, 2, 3, 4, 5]
reversed_array = reverse_array(arr)
print("Reversed array:", reversed_array)