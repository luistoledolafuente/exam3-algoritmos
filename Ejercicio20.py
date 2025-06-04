class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """🔄 AVL Tree with delete/rebalance."""
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return 0 if not node else node.height

    def get_balance(self, node):
        return 0 if not node else self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def min_value_node(self, node):
        """📏 Return node with smallest key in subtree rooted at node."""
        current = node
        while current.left:
            current = current.left
        return current

    def insert(self, node, key):
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        # LL
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)
        # RR
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)
        # LR
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        # RL
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def delete(self, node, key):
        """
        ➖ Delete key from AVL subtree rooted at node, rebalance if needed.
        """
        if not node:
            return node
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            # Node with only one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            # Node with two children: get inorder successor
            temp = self.min_value_node(node.right)
            node.key = temp.key
            node.right = self.delete(node.right, temp.key)
        if not node:
            return node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        # LL
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)
        # LR
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        # RR
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)
        # RL
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

# Helper: inorder traversal
def inorder(n, res):
    if n:
        inorder(n.left, res)
        res.append(n.key)
        inorder(n.right, res)

# 🧪 Test cases
def test_avl_delete():
    # Test 1: Delete Leaf
    tree = AVLTree()
    root = None
    for k in [20, 10, 30]:
        root = tree.insert(root, k)
    root = tree.delete(root, 10)
    result = []
    inorder(root, result)
    print("🍂 Test 1:", result == [20, 30])

    # Test 2: Delete Node with One Child
    tree = AVLTree()
    root = None
    for k in [20, 10, 30, 5]:
        root = tree.insert(root, k)
    root = tree.delete(root, 10)
    result = []
    inorder(root, result)
    print("🔄 Test 2:", result == [5, 20, 30])

    # Test 3: Delete Node with Two Children
    tree = AVLTree()
    root = None
    for k in [20, 10, 30, 5, 15]:
        root = tree.insert(root, k)
    root = tree.delete(root, 10)
    result = []
    inorder(root, result)
    print("✅ Test 3:", result == [5, 15, 20, 30])

    # Test 4: Rebalance After Deletion (LL)
    tree = AVLTree()
    root = None
    for k in [30, 20, 10, 5]:
        root = tree.insert(root, k)
    root = tree.delete(root, 5)
    result = []
    inorder(root, result)
    print("👈 Test 4:", result == [10, 20, 30])

    # Test 5: Rebalance After Deletion (RR)
    tree = AVLTree()
    root = None
    for k in [10, 20, 30, 40]:
        root = tree.insert(root, k)
    root = tree.delete(root, 10)
    result = []
    inorder(root, result)
    print("👉 Test 5:", result == [20, 30, 40])

# 🚀 Run tests
test_avl_delete()