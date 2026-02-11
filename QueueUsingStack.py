class Stack:
    def __init__(self):
        self.insert=[]
        self.delete=[]

    def enqueue(self, data):
        self.insert.append(data)
    def dequeue(self):
        if not self.delete:
            while self.insert:
                self.delete.append(self.insert.pop())
        if not self.delete:
            raise IndexError("Queue is empty")
        pop= self.delete.pop()
        print("Dequeued element:", pop)

    def peek(self):
        if not self.delete:
            while self.insert:
                self.delete.append(self.insert.pop())
        if not self.delete:
            raise IndexError("Queue is empty")
        peek= self.delete[-1]
        print("Peeked element:", peek)
        return peek
    def display(self):
        if not self.delete:
            while self.insert:
                self.delete.append(self.insert.pop())
        print("Queue elements:", self.delete[::-1])

# Example usage
queue = Stack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()  # Output: Queue elements: [1, 2, 3]
queue.dequeue()  # Output: Dequeued element: 1
queue.peek()     # Output: Peeked element: 2
queue.display()  # Output: Queue elements: [2, 3]