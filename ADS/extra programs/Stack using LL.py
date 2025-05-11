class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, value):
        """Push an element onto the stack."""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Pop the top element from the stack."""
        if self.is_empty():
            return "Stack is empty!"
        popped_value = self.top.value
        self.top = self.top.next
        return popped_value

    def peek(self):
        """Get the top element without removing it."""
        if self.is_empty():
            return "Stack is empty!"
        return self.top.value

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

# Example Usage
stack = StackLinkedList()
stack.push(10)
stack.push(20)
stack.push(30)
print("Top element:", stack.peek())  # Output: 30
print("Popped element:", stack.pop())  # Output: 30
