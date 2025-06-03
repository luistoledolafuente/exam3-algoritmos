class Node:
    """🌱 Node for Binary Search Tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """🌳 BST with insert functionality."""
    def __init__(self):
        self.root = None  # 📭 Initially empty

    def insert(self, value):
        """🧩 Insert a value into the BST."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        """🔄 Recursive helper for insert."""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            # Duplicates go to the right
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

# 🧪 Test cases
def test_insert():
    # Test 1: Insert into empty
    bst = BinarySearchTree()
    bst.insert(10)
    print("🌱 Test 1:", bst.root is not None and bst.root.value == 10)
    # Test 2: Left child
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    print("👈 Test 2:", bst.root.left is not None and bst.root.left.value == 5)
    # Test 3: Right child
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(15)
    print("👉 Test 3:", bst.root.right is not None and bst.root.right.value == 15)
    # Test 4: Deep insert
    bst = BinarySearchTree()
    for v in [10, 5, 15, 3, 7]:
        bst.insert(v)
    cond4 = (bst.root.left.left.value == 3 and bst.root.left.right.value == 7)
    print("🔄 Test 4:", cond4)
    # Test 5: Duplicates to right
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(10)
    print("🔁 Test 5:", bst.root.right is not None and bst.root.right.value == 10)

# 🚀 Run tests
test_insert()
