class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, data):
        if self.top == self.size - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return
        data = self.stack[self.top]
        self.top -= 1
        return data

    def top(self):
        if self.top == -1:
            print("Stack Underflow")
            return
        return self.stack[self.top]
