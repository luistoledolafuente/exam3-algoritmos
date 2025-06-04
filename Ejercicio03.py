class ExprNode:
    """🔢 Node for an expression tree."""
    def __init__(self, value):
        self.value = value     # Operator (str) or operand (str/number)
        self.left = None       # ↙️ Left child
        self.right = None      # ↘️ Right child

class ExpressionTree:
    """📝 Binary tree for building and traversing expressions."""
    def __init__(self):
        self.root = None       # 🌱 Root of the expression tree

    def build_from_prefix(self, prefix_tokens):
        """🔨 Build expression tree from prefix notation."""
        def helper(tokens):
            if not tokens:
                return None
            token = tokens.pop(0)
            node = ExprNode(token)
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
    cond1 = (tree.root and tree.root.value == "+" and 
             tree.root.left.value == "2" and tree.root.right.value == "3")
    print("🌳 Test 1:", cond1)
    # Test 2
    tree = ExpressionTree()
    tree.build_from_prefix(["*", "+", "1", "2", "3"])
    cond2 = (tree.root and tree.root.value == "*" and 
             tree.root.left.value == "+" and 
             tree.root.left.left.value == "1" and tree.root.left.right.value == "2" and 
             tree.root.right.value == "3")
    print("🌳 Test 2:", cond2)
    # Test 3
    tree = ExpressionTree()
    tree.build_from_prefix(["-", "x", "y"])
    cond3 = (tree.root and tree.root.value == "-" and 
             tree.root.left.value == "x" and tree.root.right.value == "y")
    print("🌳 Test 3:", cond3)
    # Test 4
    tree = ExpressionTree()
    tree.build_from_prefix(["-", "*", "2", "3", "/", "8", "4"])
    cond4 = (tree.root and tree.root.value == "-" and 
             tree.root.left.value == "*" and tree.root.right.value == "/")
    print("🌳 Test 4:", cond4)
    # Test 5: Empty list
    tree = ExpressionTree()
    tree.build_from_prefix([])
    print("🌳 Test 5:", tree.root is None)

# 🚀 Run tests
test_build_from_prefix() 