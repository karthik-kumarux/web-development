class BTreeNode:
    def __init__(self, is_leaf=True):
        self.is_leaf = is_leaf
        self.keys = []  # List of keys in the node
        self.children = []  # List of child nodes


class BTree:
    def __init__(self, order=5):
        self.root = BTreeNode()
        self.order = order

    def search(self, node, key):
        """Search for a key in the B-tree"""
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return True
        if node.is_leaf:
            return False
        return self.search(node.children[i], key)

    def insert(self, key):
        """Insert a key into the B-tree"""
        root = self.root
        if len(root.keys) == self.order - 1:
            new_node = BTreeNode(is_leaf=False)
            new_node.children.append(self.root)
            self.split(new_node, 0)
            self.root = new_node
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        """Insert key into a non-full node"""
        if node.is_leaf:
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            node.keys.insert(i + 1, key)
        else:
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == self.order - 1:
                self.split(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def split(self, parent, index):
        """Split a full node"""
        node = parent.children[index]
        mid = len(node.keys) // 2
        new_node = BTreeNode(is_leaf=node.is_leaf)
        parent.keys.insert(index, node.keys[mid])
        parent.children.insert(index + 1, new_node)

        new_node.keys = node.keys[mid + 1:]
        node.keys = node.keys[:mid]

        if not node.is_leaf:
            new_node.children = node.children[mid + 1:]
            node.children = node.children[:mid + 1]

    def delete(self, key):
        """Delete a key from the B-tree"""
        self._delete(self.root, key)
        if len(self.root.keys) == 0 and not self.root.is_leaf:
            self.root = self.root.children[0]

    def _delete(self, node, key):
        """Helper function for deleting a key"""
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            if node.is_leaf:
                node.keys.pop(i)
            else:
                self._delete_internal(node, i)
        elif not node.is_leaf:
            self._delete_from_child(node, i, key)

    def _delete_internal(self, node, index):
        """Delete a key from a non-leaf node"""
        left_child = node.children[index]
        right_child = node.children[index + 1]
        if len(left_child.keys) >= (self.order + 1) // 2: # Corrected to (order+1)//2
            self._delete_predecessor(node, index)
        elif len(right_child.keys) >= (self.order + 1) // 2: # corrected to (order+1)//2
            self._delete_successor(node, index)
        else:
            self._merge(node, index)

    def _delete_predecessor(self, node, index):
        """Get the predecessor of a key and delete it"""
        child = node.children[index]
        predecessor = child.keys[-1]
        self._delete(child, predecessor)
        node.keys[index] = predecessor

    def _delete_successor(self, node, index):
        """Get the successor of a key and delete it"""
        child = node.children[index + 1]
        successor = child.keys[0]
        self._delete(child, successor)
        node.keys[index] = successor

    def _merge(self, node, index):
        """Merge two children into one"""
        left_child = node.children[index]
        right_child = node.children[index + 1]
        left_child.keys.append(node.keys[index])
        left_child.keys.extend(right_child.keys)
        left_child.children.extend(right_child.children)
        node.keys.pop(index)
        node.children.pop(index + 1)

    def _delete_from_child(self, node, index, key):
        """Delete key from a child node"""
        child = node.children[index]
        if len(child.keys) < (self.order - 1) // 2: # corrected to (order-1)//2
            self._fill(node, index)
        self._delete(node.children[index], key)

    def _fill(self, node, index):
        """Fill the child node if it has fewer than half of the keys"""
        if index > 0 and len(node.children[index - 1].keys) >= (self.order + 1) // 2: # Corrected to (order+1)//2
            self._borrow_from_prev(node, index)
        elif index < len(node.children) - 1 and len(node.children[index + 1].keys) >= (self.order + 1) // 2: # Corrected to (order+1)//2
            self._borrow_from_next(node, index)
        else:
            if index < len(node.children) - 1:
                self._merge(node, index)
            else:
                self._merge(node, index - 1)

    def _borrow_from_prev(self, node, index):
        """Borrow a key from the previous sibling"""
        child = node.children[index]
        sibling = node.children[index - 1]
        child.keys.insert(0, node.keys[index - 1])
        node.keys[index - 1] = sibling.keys.pop()
        if not sibling.is_leaf:
            child.children.insert(0, sibling.children.pop())

    def _borrow_from_next(self, node, index):
        """Borrow a key from the next sibling"""
        child = node.children[index]
        sibling = node.children[index + 1]
        child.keys.append(node.keys[index])
        node.keys[index] = sibling.keys.pop(0)
        if not sibling.is_leaf:
            child.children.append(sibling.children.pop(0))


# Dynamic Input
def dynamic_input():
    # Read number of elements
    num_elements = int(input("Enter the number of elements to insert into the B-tree: "))

    # Read elements
    elements = []
    print(f"Enter {num_elements} elements:")
    for _ in range(num_elements):
        element = int(input())
        elements.append(element)

    # Create B-Tree of order 5
    b_tree = BTree(order=5)

    # Insert elements into the B-tree
    for elem in elements:
        b_tree.insert(elem)

    # Read key for search operation
    search_key = int(input("Enter the key to search for: "))
    if b_tree.search(b_tree.root, search_key):
        print(f"Key {search_key} found in the B-tree.")
    else:
        print(f"Key {search_key} not found in the B-tree.")

    # Read key for delete operation
    delete_key = int(input("Enter the key to delete from the B-tree: "))
    b_tree.delete(delete_key)

    # Verify deletion
    if b_tree.search(b_tree.root, delete_key):
        print(f"Key {delete_key} is still present after deletion.")
    else:
        print(f"Key {delete_key} successfully deleted.")


# Run the dynamic input function
dynamic_input()
