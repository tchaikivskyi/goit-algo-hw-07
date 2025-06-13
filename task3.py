class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value)

    def sum_values(self):
        def _sum(node):
            if node is None:
                return 0
            return node.value + _sum(node.left) + _sum(node.right)
        return _sum(self.root)


if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [20, 10, 30, 5, 15, 25, 35]
    for val in values:
        bst.insert(val)

    print("Сума всіх значень у дереві:", bst.sum_values()) 
