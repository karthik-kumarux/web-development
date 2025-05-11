class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf  # True if the node is a leaf
        self.keys = []  # Store keys
        self.children = []  # Store child nodes

def inorder_traversal(node, result):
    """Perform inorder traversal to extract keys."""
    if node:
        for i in range(len(node.keys)):
            if len(node.children) > i:
                inorder_traversal(node.children[i], result)
            result.append(node.keys[i])
        if len(node.children) > len(node.keys):
            inorder_traversal(node.children[-1], result)

def merge_sorted_keys(keys1, keys2):
    """Merge two sorted key lists."""
    return sorted(keys1 + keys2)

def build_balanced_btree(keys, min_degree):
    """Build a balanced B-Tree from sorted keys."""
    if not keys:
        return None

    mid = len(keys) // 2
    root = BTreeNode()
    root.keys.append(keys[mid])

    left_keys = keys[:mid]
    right_keys = keys[mid+1:]

    if left_keys:
        root.children.append(build_balanced_btree(left_keys, min_degree))
    if right_keys:
        root.children.append(build_balanced_btree(right_keys, min_degree))

    return root

def merge_btrees(root1, root2, min_degree):
    """Merge two B-Trees into one."""
    keys1, keys2 = [], []
    inorder_traversal(root1, keys1)
    inorder_traversal(root2, keys2)
    
    merged_keys = merge_sorted_keys(keys1, keys2)
    return build_balanced_btree(merged_keys, min_degree)

# Example Usage:
btree1 = BTreeNode()
btree1.keys = [10, 20, 30]

btree2 = BTreeNode()
btree2.keys = [15, 25, 35]

merged_tree = merge_btrees(btree1, btree2, min_degree=2)
print("Merged B-Tree Root Keys:", merged_tree.keys)  # Expected: [20]
