class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """⚙️ AVL Tree with insert/rebalance."""
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

    def insert(self, node, key):
        """
        ➕ Insert key into AVL subtree rooted at node, rebalance if needed, return new root.
        """
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

# 🧪 Test cases
def test_avl_insert():
    tree = AVLTree()
    # Test 1: Simple Insert
    root = tree.insert(None, 10)
    print("🌱 Test 1:", root.key == 10 and root.height == 1)

    # Test 2: LL Case [30,20,10]
    root = None
    for k in [30, 20, 10]:
        root = tree.insert(root, k)
    cond2 = (root.key == 20 and root.left.key == 10 and root.right.key == 30)
    print("➙ Test 2:", cond2)

    # Test 3: RR Case [10,20,30]
    root = None
    for k in [10, 20, 30]:
        root = tree.insert(root, k)
    cond3 = (root.key == 20 and root.left.key == 10 and root.right.key == 30)
    print("➙ Test 3:", cond3)

    # Test 4: LR Case [30,10,20]
    root = None
    for k in [30, 10, 20]:
        root = tree.insert(root, k)
    cond4 = (root.key == 20 and root.left.key == 10 and root.right.key == 30)
    print("🔄 Test 4:", cond4)

    # Test 5: RL Case [10,30,20]
    root = None
    for k in [10, 30, 20]:
        root = tree.insert(root, k)
    cond5 = (root.key == 20 and root.left.key == 10 and root.right.key == 30)
    print("🔁 Test 5:", cond5)

# 🚀 Run tests
test_avl_insert()