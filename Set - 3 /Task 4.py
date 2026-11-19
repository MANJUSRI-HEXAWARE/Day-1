class HospitalQueue:
   def __init__(self, capacity):
     self.capacity = capacity
     self.items = [None] * capacity
     self.front = 0
     self.rear = -1
     self.count = 0
   def enqueue(self, patient):
     if self.count == self.capacity:
        print("Queue is full. Cannot add:", patient)
        return
     self.rear = (self.rear + 1) % self.capacity
     self.items[self.rear] = patient
     self.count += 1
   def dequeue(self):
     if self.count == 0:
        print("Queue is empty.")
        return None
     patient = self.items[self.front]
     self.items[self.front] = None
     self.front = (self.front + 1) % self.capacity
     self.count -= 1
     return patient
   def display(self):
     print("Walk-in token queue:", end=" ")
     for i in range(self.count):
        index = (self.front + i) % self.capacity
        print(self.items[index], end=" ")
     print()
class PatientHistoryStack:
   def __init__(self, capacity):
     self.capacity = capacity
     self.items = [None] * capacity
     self.top = -1
   def push(self, patient):
     if self.top == self.capacity - 1:
        print("History is full. Cannot add:", patient)
        return
     self.top += 1
     self.items[self.top] = patient
   def pop(self):
     if self.top == -1:
        print("Patient history is empty.")
        return None
     patient = self.items[self.top]
     self.items[self.top] = None
     self.top -= 1
     return patient
   def peek(self):
     if self.top == -1:
        print("Patient history is empty.")
        return None
     return self.items[self.top]
   def display(self):
     print("Recently viewed patients (latest first):", end=" ")
     for i in range(self.top, -1, -1):
        print(self.items[i], end=" ")
     print()
print("HOSPITAL WALK-IN TOKEN QUEUE")
print("----------------------------")
walk_in_queue = HospitalQueue(5)
walk_in_queue.enqueue("P100021")
walk_in_queue.enqueue("P100022")
walk_in_queue.enqueue("P100023")
walk_in_queue.display()
print("Serving patient:", walk_in_queue.dequeue())
walk_in_queue.display()
print("\nRECENTLY VIEWED PATIENT HISTORY")
print("--------------------------------")
history = PatientHistoryStack(5)
history.push("P100101")
history.push("P100102")
history.push("P100103")
history.display()
print("Most recently viewed patient:", history.peek())
print("Removing latest viewed patient:", history.pop())
history.display()
