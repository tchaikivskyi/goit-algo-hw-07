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

    def find_min(self):
        current = self.root
        if not current:
            return None  
        while current.left:
            current = current.left
        return current.value


if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [20, 10, 30, 5, 15, 25, 35]
    for val in values:
        bst.insert(val)

    print("Найменше значення в дереві:", bst.find_min())  
