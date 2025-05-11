import os

# Define the AVL Tree Node class
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # height of the node

# Define the AVL Tree class
class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        return 0 if not node else node.height

    def balance_factor(self, node):
        return 0 if not node else self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return y

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = max(self.height(root.left), self.height(root.right)) + 1
        balance = self.balance_factor(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        root.height = max(self.height(root.left), self.height(root.right)) + 1
        balance = self.balance_factor(root)

        if balance > 1 and self.balance_factor(root.left) >= 0:
            return self.right_rotate(root)

        if balance < -1 and self.balance_factor(root.right) <= 0:
            return self.left_rotate(root)

        if balance > 1 and self.balance_factor(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.balance_factor(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def inorder(self, root):
        result = []
        if root:
            result.extend(self.inorder(root.left))
            result.append(root.key)
            result.extend(self.inorder(root.right))
        return result

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def delete_key(self, key):
        self.root = self.delete(self.root, key)

    def write_inorder_to_file(self, filename):
        with open(filename, 'w') as f:
            inorder_result = self.inorder(self.root)
            f.write(" ".join(map(str, inorder_result)) + "\n")

    def bst_inorder_traversal(self):
        return self.inorder(self.root)

def process_avl_tree():
    # Ask the user for input and output file names
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")

    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"File '{input_file}' does not exist. Please provide a valid file.")
        return

    # Read elements from the input file
    with open(input_file, 'r') as f:
        elements = list(map(int, f.read().split()))

    # Initialize AVL Tree
    avl_tree = AVLTree()

    # Insert elements from the file into the AVL tree
    for elem in elements:
        avl_tree.insert_key(elem)

    # Start the menu-driven interaction
    while True:
        print("\n--- AVL Tree Operations ---")
        print("1. Insert element")
        print("2. Delete element")
        print("3. BST In-order Traversal")
        print("4. Save tree to file and Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            # Insert element
            element = int(input("Enter element to insert: "))
            avl_tree.insert_key(element)
            print(f"Element {element} inserted.")
            print("Current In-order Traversal:", avl_tree.bst_inorder_traversal())
        
        elif choice == '2':
            # Delete element
            element = int(input("Enter element to delete: "))
            avl_tree.delete_key(element)
            print(f"Element {element} deleted.")
            print("Current In-order Traversal:", avl_tree.bst_inorder_traversal())
        
        elif choice == '3':
            # Perform BST In-order traversal
            print("BST In-order Traversal:", avl_tree.bst_inorder_traversal())
        
        elif choice == '4':
            # Save tree to file and exit
            avl_tree.write_inorder_to_file(output_file)  # Saving to a separate output file
            print(f"AVL tree saved to {output_file}. Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Call the process function
process_avl_tree()
