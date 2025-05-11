class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf  # True if the node is a leaf
        self.keys = []  # Store keys
        self.children = []  # Store child nodes

def get_height(node):
    if node is None:
        return 0
    
    if node.leaf:
        return 1  # Leaf node height is 1

    # Recursively calculate height from the child nodes
    return 1 + max(get_height(child) for child in node.children)

# Example usage:
root = BTreeNode()
child1 = BTreeNode()
child2 = BTreeNode(leaf=True)
root.children.append(child1)
child1.children.append(child2)

print("Height of the B-tree:", get_height(root))  # Expected output: 3
