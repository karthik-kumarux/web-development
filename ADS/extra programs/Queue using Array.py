class QueueArray:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        """Add an element to the queue."""
        self.queue.append(value)

    def dequeue(self):
        """Remove an element from the front of the queue."""
        if self.is_empty():
            return "Queue is empty!"
        return self.queue.pop(0)

    def peek(self):
        """Get the front element without removing it."""
        if self.is_empty():
            return "Queue is empty!"
        return self.queue[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the size of the queue."""
        return len(self.queue)

# Example Usage
queue = QueueArray()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Front element:", queue.peek())  # Output: 10
print("Queue size:", queue.size())     # Output: 3
print("Dequeued element:", queue.dequeue())  # Output: 10
