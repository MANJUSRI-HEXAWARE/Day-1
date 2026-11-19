SIZE = 5
class Queue:
    def __init__(self):
        self.items = [None] * SIZE
        self.front = 0
        self.rear = -1
        self.count = 0
    def enqueue(self, transaction):
        if self.count == SIZE:
            print("Queue is full")
            return
        self.rear = (self.rear + 1) % SIZE
        self.items[self.rear] = transaction
        self.count += 1
        print("Added to review:", transaction)
    def dequeue(self):
        if self.count == 0:
            print("Queue is empty")
            return
        transaction = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % SIZE
        self.count -= 1
        print("Reviewed and removed:", transaction)
    def display(self):
        print("Review backlog:", end=" ")
        if self.count == 0:
            print("Empty")
            return
        for i in range(self.count):
            index = (self.front + i) % SIZE
            print(self.items[index], end=" ")
        print()
class Stack:
    def __init__(self, balance):
        self.items = [None] * SIZE
        self.top = -1
        self.balance = balance
    def push(self, adjustment):
        if self.top == SIZE - 1:
            print("Stack is full")
            return
        self.top += 1
        self.items[self.top] = adjustment
        self.balance += adjustment
        print("Adjustment applied:", adjustment)
        print("Current balance: Rs.", self.balance)
    def pop(self):
        if self.top == -1:
            print("No adjustment to reverse")
            return
        adjustment = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        self.balance -= adjustment
        print("Last adjustment reversed:", adjustment)
        print("Restored balance: Rs.", self.balance)
    def peek(self):
        if self.top == -1:
            print("No adjustments available")
        else:
            print("Latest adjustment:", self.items[self.top])
    def display(self):
        print("Adjustment history (latest first):", end=" ")
        if self.top == -1:
            print("Empty")
            return
        for i in range(self.top, -1, -1):
            print(self.items[i], end=" ")
        print()
print("QUEUE - MANUAL REVIEW BACKLOG")
q = Queue()
q.enqueue("T301")
q.enqueue("T302")
q.enqueue("T303")
q.display()
q.dequeue()
q.enqueue("T304")
q.display()
print("\nSTACK - REVERSE LAST ADJUSTMENT")
s = Stack(10000)
print("Initial balance: Rs.", s.balance)
s.push(500)
s.push(-200)
s.push(300)
s.display()
s.peek()
s.pop()
s.display()
