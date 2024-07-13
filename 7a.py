class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item}.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        item = self.items.pop()
        print(f"Popped {item}.")
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack:", self.items)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued {item}.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        item = self.items.pop(0)
        print(f"Dequeued {item}.")
        return item

    def front(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print("Queue:", self.items)

def test_stack():
    print("\nTesting Stack Operations:")
    stack = Stack()
    while True:
        action = input("Choose an action - push (p), pop (o), peek (k), display (d), or quit (q): ").lower()
        if action == 'q':
            break
        elif action == 'p':
            item = input("Enter value to push: ")
            stack.push(item)
        elif action == 'o':
            stack.pop()
        elif action == 'k':
            top_item = stack.peek()
            if top_item is not None:
                print("Top:", top_item)
        elif action == 'd':
            stack.display()
        else:
            print("Invalid action.")
        stack.display()

def test_queue():
    print("\nTesting Queue Operations:")
    queue = Queue()
    while True:
        action = input("Choose an action - enqueue (e), dequeue (d), front (f), display (y), or quit (q): ").lower()
        if action == 'q':
            break
        elif action == 'e':
            item = input("Enter value to enqueue: ")
            queue.enqueue(item)
        elif action == 'd':
            queue.dequeue()
        elif action == 'f':
            front_item = queue.front()
            if front_item is not None:
                print("Front:", front_item)
        elif action == 'y':
            queue.display()
        else:
            print("Invalid action.")
        queue.display()

test_stack()
test_queue()
