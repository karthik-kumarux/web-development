class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """Add an element to the queue."""
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """Remove an element from the front of the queue."""
        if self.is_empty():
            return "Queue is empty!"
        dequeued_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_value

    def peek(self):
        """Get the front element without removing it."""
        if self.is_empty():
            return "Queue is empty!"
        return self.front.value

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front is None

# Example Usage
queue = QueueLinkedList()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Front element:", queue.peek())  # Output: 10
print("Dequeued element:", queue.dequeue())  # Output: 10
