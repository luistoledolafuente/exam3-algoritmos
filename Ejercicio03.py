class Node:
    """Node for an expression tree node."""
    def __init__(self, value):
        self.value = value        # Operator or operand (string)
        self.left = None          # Left child (Node or None)
        self.right = None         # Right child (Node or None)

class ExpressionTree:
    """Binary tree for mathematical expressions."""
    def __init__(self):
        self.root = None  # 🌱 Root of expression tree

    def build_from_prefix(self, prefix_tokens):
        """🔨 Build expression tree from prefix notation."""
        def helper(tokens):
            if not tokens:
                return None
            token = tokens.pop(0)
            node = Node(token)
            if token in {"+", "-", "*", "/"}:
                node.left = helper(tokens)
                node.right = helper(tokens)
            return node
        
        self.root = helper(prefix_tokens.copy())

# 🧪 Test cases
def test_build_from_prefix():
    tree = ExpressionTree()
    # Test 1
    tree.build_from_prefix(["+", "2", "3"])
    print("🌳 Test 1:", tree.root.value == "+" and tree.root.left.value == "2" and tree.root.right.value == "3")  # ✅
    # Test 2
    tree = ExpressionTree()
    tree.build_from_prefix(["*", "+", "1", "2", "3"])
    print("🌳 Test 2:", tree.root.value == "*" and tree.root.left.value == "+" and tree.root.right.value == "3")  # ✅
    # Test 3
    tree = ExpressionTree()
    tree.build_from_prefix(["-", "x", "y"])
    print("🌳 Test 3:", tree.root.value == "-" and tree.root.left.value == "x" and tree.root.right.value == "y")  # ✅
    # Test 4
    tree = ExpressionTree()
    tree.build_from_prefix(["-", "*", "2", "3", "/", "8", "4"])
    print("🌳 Test 4:", tree.root.value == "-" and tree.root.left.value == "*" and tree.root.right.value == "/")  # ✅
    # Test 5
    tree = ExpressionTree()
    tree.build_from_prefix([])
    print("🌳 Test 5:", tree.root is None)  # 📭

# 🚀 Run tests
test_build_from_prefix()