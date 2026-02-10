class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "pushed into stack")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        temp = self.top
        print("Stack elements:")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print("Top element:", s.peek())

print("Popped element:", s.pop())

s.display()
