class StackArray:
    def __init__(self):
        self.stack = []

    def push(self, value):
        """Push an element onto the stack."""
        self.stack.append(value)

    def pop(self):
        """Pop the top element from the stack."""
        if self.is_empty():
            return "Stack is empty!"
        return self.stack.pop()

    def peek(self):
        """Get the top element without removing it."""
        if self.is_empty():
            return "Stack is empty!"
        return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the size of the stack."""
        return len(self.stack)

# Example Usage
stack = StackArray()
stack.push(10)
stack.push(20)
stack.push(30)
print("Top element:", stack.peek())  # Output: 30
print("Stack size:", stack.size())   # Output: 3
print("Popped element:", stack.pop())  # Output: 30
