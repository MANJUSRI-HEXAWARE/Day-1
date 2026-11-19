
from collections import deque


class CustomStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None

        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


class CustomQueue:
    def __init__(self):
        self.items = []
        self.front = 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None

        item = self.items[self.front]
        self.front += 1

        if self.front == len(self.items):
            self.items = []
            self.front = 0

        return item

    def is_empty(self):
        return self.front == len(self.items)


def main():
    print("=" * 65)
    print("TASK 4 - STACK AND QUEUE OPERATIONS")
    print("=" * 65)

    print("\nCUSTOM STACK - UNDO LAST ORDER EDIT")
    print("-" * 65)

    order = {
        "orderId": "ORD1001",
        "amount": 2000
    }

    undo_stack = CustomStack()

    print("Original Order Amount :", order["amount"])

    undo_stack.push(order["amount"])
    order["amount"] = 2500

    print("After First Edit :", order["amount"])

    undo_stack.push(order["amount"])
    order["amount"] = 3000

    print("After Second Edit :", order["amount"])

    previous_amount = undo_stack.pop()

    if previous_amount is not None:
        order["amount"] = previous_amount

    print("After Undo          :", order["amount"])
    print("Remaining Stack         :", undo_stack.items)

    print("\nCUSTOM QUEUE - WAREHOUSE DISPATCH")
    print("-" * 65)

    dispatch_queue = CustomQueue()

    orders = ["ORD1001", "ORD1002", "ORD1003", "ORD1004"]

    for order_id in orders:
        dispatch_queue.enqueue(order_id)

    print("Orders Added:", orders)

    print("\nDispatch Order:")

    while not dispatch_queue.is_empty():
        print("Dispatched:", dispatch_queue.dequeue())

    print("\nBUILT-IN STACK USING PYTHON LIST")
    print("-" * 65)

    builtin_stack = []

    builtin_order = {
        "orderId": "ORD1002",
        "amount": 2000
    }

    print("Original Order Amount :", builtin_order["amount"])

    builtin_stack.append(builtin_order["amount"])
    builtin_order["amount"] = 2500

    print("After First Edit :", builtin_order["amount"])

    builtin_stack.append(builtin_order["amount"])
    builtin_order["amount"] = 3000

    print("After Second Edit :", builtin_order["amount"])

    builtin_order["amount"] = builtin_stack.pop()

    print("After Undo          :", builtin_order["amount"])

    print("\nBUILT-IN QUEUE USING DEQUE")
    print("-" * 65)

    builtin_queue = deque()

    for order_id in orders:
        builtin_queue.append(order_id)

    print("Orders Added:", orders)

    print("\nDispatch Order:")

    while builtin_queue:
        print("Dispatched:", builtin_queue.popleft())

    print("\n" + "=" * 65)
    print("CUSTOM VS BUILT-IN DATA STRUCTURES")
    print("=" * 65)

    print(f"{'Operation':<22}{'Custom':<20}{'Built-in'}")
    print("-" * 65)

    print(f"{'Stack Insertion':<22}{'push()':<20}{'append()'}")
    print(f"{'Stack Deletion':<22}{'pop()':<20}{'pop()'}")
    print(f"{'Queue Insertion':<22}{'enqueue()':<20}{'append()'}")
    print(f"{'Queue Deletion':<22}{'dequeue()':<20}{'popleft()'}")

    print("-" * 65)

    print("\nCUSTOM AND BUILT-IN OPERATIONS EXECUTED SUCCESSFULLY")
    print("TASK 4 EXECUTION COMPLETED")


if __name__ == "__main__":
    main()
