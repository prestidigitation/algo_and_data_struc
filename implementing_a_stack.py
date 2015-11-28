class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if len(self.items) < 1:
            return "No items in stack to pop!"
        return self.items.pop()

    def peek(self):
        if len(self.items) < 1:
            return "No items in stack to peek at!"
        return self.items[-1]

    def size(self):
        return len(self.items)


## Write a function revstring(mystr) that uses a stack to reverse the characters in ## a string.

def rev_string(my_string):
    stack = Stack()
    reversed_string = []
    for letter in my_string:
        stack.push(letter)
    while stack.is_empty() == False:
        reversed_string += stack.pop()
    return ''.join(reversed_string)

