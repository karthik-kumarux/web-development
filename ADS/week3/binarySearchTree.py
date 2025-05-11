class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.value:
            if node.left:
                self._insert(node.left, key)
            else:
                node.left = Node(key)
        else:
            if node.right:
                self._insert(node.right, key)
            else:
                node.right = Node(key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.value == key:
            return node
        return self._search(node.left if key < node.value else node.right, key)

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.value] + self._inorder(node.right)


# Usage example: Dynamic input
bst = BST()

while True:
    print("\n1. Insert a node")
    print("2. Search for a node")
    print("3. Show Inorder Traversal")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        value = int(input("Enter the value to insert: "))
        bst.insert(value)
        print(f"Node {value} inserted.")
    
    elif choice == '2':
        value = int(input("Enter the value to search: "))
        result = bst.search(value)
        print(f"Node with key {value} {'found' if result else 'not found'}")
    
    elif choice == '3':
        print("Inorder Traversal:", bst.inorder())  # Output sorted order

    elif choice == '4':
        print("Exiting...")
        break
    
    else:
        print("Invalid choice! Please try again.")
