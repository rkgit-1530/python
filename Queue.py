class Queue:
    def __init__(self,size):
        self.items = []
        self.front=-1
        self.rear=-1
        self.size=size

    def enqueue(self,data):
        if self.rear==self.size-1:
            print("Queue Full")
        else:
            if self.front == -1:
                self.front+=1
            self.rear= self.rear+1
            self.items.append(data)
            print(f'{data} has been added')
    def dequeue(self):
        if self.front==-1:
            print("Queue is Empty")
        else:
            print(f'{self.items[self.front]} has been deleted')
            self.front+=1
            if self.front == -1:
                self.front , self.rear=-1
    def peek(self):
        if self.front==-1:
            print("queue is Empty")
        else:
            print(f"Peeked Element is {self.items[self.front]}")
    
    def isEmpty(self):
        if self.front==-1:
            print("Queue is Empty")
            return True
    
    def isFull(self):
        if self.rear==self.size-1:
            print("Queue is Full")
    
    def display(self):
        if self.isEmpty:
            print("Queue is Empty")
        else:
            for i in range(self.front,self.rear+1):
                print(self.items[i],end="->")

size=int(input("Enter Size: "))  
queue=Queue(size)
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
queue.enqueue(20)
queue.dequeue()
queue.dequeue()
queue.display()