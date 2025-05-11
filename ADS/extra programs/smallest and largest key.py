class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_rec(node.left, key)
        else:
            node.right = self._insert_rec(node.right, key)
        return node

    # Function to find the smallest (minimum) key
    def find_min(self):
        return self._find_min_rec(self.root)

    def _find_min_rec(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node.key

    # Function to find the largest (maximum) key
    def find_max(self):
        return self._find_max_rec(self.root)

    def _find_max_rec(self, node):
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node.key

# Example usage
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Smallest key:", bst.find_min())  # Expected output: 20
print("Largest key:", bst.find_max())   # Expected output: 80
