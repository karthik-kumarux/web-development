import random

ORDER = 5

class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self):
        self.root = BTreeNode(leaf=True)

    def search(self, key, node=None, level=0):
        if node is None:
            node = self.root

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return True, level
        elif node.leaf:
            return False, -1
        else:
            return self.search(key, node.children[i], level + 1)

    def insert(self, key):
        root = self.root
        if len(root.keys) == ORDER - 1:
            new_node = BTreeNode()
            new_node.children.insert(0, self.root)
            self._split_child(new_node, 0)
            self.root = new_node
            self._insert_non_full(new_node, key)
        else:
            self._insert_non_full(root, key)

    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == ORDER - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent, i):
        t = ORDER // 2
        y = parent.children[i]
        z = BTreeNode(leaf=y.leaf)

        parent.keys.insert(i, y.keys[t])
        parent.children.insert(i + 1, z)

        z.keys = y.keys[t + 1:]
        y.keys = y.keys[:t]

        if not y.leaf:
            z.children = y.children[t + 1:]
            y.children = y.children[:t + 1]

    def delete(self, key):
        level_deleted = self._delete(self.root, key, 0)
        if len(self.root.keys) == 0 and not self.root.leaf:
            self.root = self.root.children[0]
        return level_deleted

    def _delete(self, node, key, level):
        t = ORDER // 2
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if node.leaf:
            if i < len(node.keys) and node.keys[i] == key:
                node.keys.pop(i)
                return level
            return -1

        if i < len(node.keys) and node.keys[i] == key:
            return self._delete_internal_node(node, key, i, level)
        elif len(node.children[i].keys) >= t:
            return self._delete(node.children[i], key, level + 1)
        else:
            self._fix_child(node, i)
            return self._delete(node.children[i], key, level + 1)

    def _delete_internal_node(self, node, key, i, level):
        t = ORDER // 2
        if len(node.children[i].keys) >= t:
            pred = self._get_predecessor(node.children[i])
            node.keys[i] = pred
            self._delete(node.children[i], pred, level + 1)
        elif len(node.children[i + 1].keys) >= t:
            succ = self._get_successor(node.children[i + 1])
            node.keys[i] = succ
            self._delete(node.children[i + 1], succ, level + 1)
        else:
            self._merge(node, i)
            self._delete(node.children[i], key, level + 1)
        return level

    def _get_predecessor(self, node):
        while not node.leaf:
            node = node.children[-1]
        return node.keys[-1]

    def _get_successor(self, node):
        while not node.leaf:
            node = node.children[0]
        return node.keys[0]

    def _merge(self, node, i):
        child = node.children[i]
        sibling = node.children[i + 1]
        child.keys.append(node.keys[i])
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.children.extend(sibling.children)
        node.keys.pop(i)
        node.children.pop(i + 1)

    def _fix_child(self, node, i):
        t = ORDER // 2
        if i > 0 and len(node.children[i - 1].keys) >= t:
            left = node.children[i - 1]
            child = node.children[i]
            child.keys.insert(0, node.keys[i - 1])
            if not left.leaf:
                child.children.insert(0, left.children.pop())
            node.keys[i - 1] = left.keys.pop()
        elif i < len(node.children) - 1 and len(node.children[i + 1].keys) >= t:
            right = node.children[i + 1]
            child = node.children[i]
            child.keys.append(node.keys[i])
            if not right.leaf:
                child.children.append(right.children.pop(0))
            node.keys[i] = right.keys.pop(0)
        else:
            if i < len(node.children) - 1:
                self._merge(node, i)
            else:
                self._merge(node, i - 1)

    def print_tree(self):
        print("BTree Structure:")
        self._print_level(self.root)

    def _print_level(self, node, level=0, levels=None):
        if levels is None:
            levels = {}

        if level not in levels:
            levels[level] = []

        levels[level].append(node.keys[:])

        if not node.leaf:
            for child in node.children:
                self._print_level(child, level + 1, levels)

        if level == 0:
            for lvl in sorted(levels.keys()):
                print(f"Level {lvl}: {levels[lvl]}")

    def get_level_keys(self, target_level):
        levels = {}
        self._collect_levels(self.root, levels)
        return levels.get(target_level, [])

    def _collect_levels(self, node, levels, level=0):
        if level not in levels:
            levels[level] = []

        levels[level].append(node.keys[:])

        if not node.leaf:
            for child in node.children:
                self._collect_levels(child, levels, level + 1)


# ------------------------
# Run Program
# ------------------------
if __name__ == "__main__":
    bt = BTree()
    elements = random.sample(range(1, 100), 10)
    for el in elements:
        bt.insert(el)

    bt.print_tree()

    search_key = int(input("\nEnter a key to search: "))
    found, level = bt.search(search_key)
    if found:
        print(f"Key {search_key} found at level {level}")
    else:
        print(f"Key {search_key} not found in the B-tree.")

    del_key = int(input("\nEnter a key to delete: "))
    level_deleted = bt.delete(del_key)

    if level_deleted == -1:
        print(f"Key {del_key} not found for deletion.")
    else:
        print(f"Key {del_key} deleted from level {level_deleted}.")
        remaining = bt.get_level_keys(level_deleted)
        print(f"Remaining elements at level {level_deleted}: {remaining}")
