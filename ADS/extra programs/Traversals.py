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

    # Inorder traversal (Left, Root, Right)
    def inorder_traversal(self):
        return self._inorder_rec(self.root, [])

    def _inorder_rec(self, node, result):
        if node:
            self._inorder_rec(node.left, result)
            result.append(node.key)
            self._inorder_rec(node.right, result)
        return result

    # Preorder traversal (Root, Left, Right)
    def preorder_traversal(self):
        return self._preorder_rec(self.root, [])

    def _preorder_rec(self, node, result):
        if node:
            result.append(node.key)
            self._preorder_rec(node.left, result)
            self._preorder_rec(node.right, result)
        return result

    # Postorder traversal (Left, Right, Root)
    def postorder_traversal(self):
        return self._postorder_rec(self.root, [])

    def _postorder_rec(self, node, result):
        if node:
            self._postorder_rec(node.left, result)
            self._postorder_rec(node.right, result)
            result.append(node.key)
        return result

# Example usage
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder traversal:", bst.inorder_traversal())   # Left, Root, Right
print("Preorder traversal:", bst.preorder_traversal())  # Root, Left, Right
print("Postorder traversal:", bst.postorder_traversal()) # Left, Right, Root
