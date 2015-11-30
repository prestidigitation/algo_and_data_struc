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


##

def infix_to_postfix(infix_expression):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expression.split()
    
    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty() and \
                (prec[op_stack.peek()] >= prec[token])):
                    postfix_list.append(op_stack.pop())
            op_stack.push(token)
    
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)
