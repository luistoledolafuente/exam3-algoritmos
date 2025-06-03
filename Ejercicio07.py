class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_operator(self):
        return self.value in ['+', '-', '*', '/']

class ExpressionTree:
    def __init__(self):
        self.root = None

    def build_from_postfix(self, postfix_tokens):
        """🔨 Build tree from postfix tokens using a stack."""
        stack = []
        for token in postfix_tokens:
            node = Node(token)
            if node.is_operator():
                node.right = stack.pop()
                node.left = stack.pop()
            stack.append(node)
        self.root = stack.pop() if stack else None

class EvaluableExpressionTree(ExpressionTree):
    def __init__(self):
        super().__init__()

    def evaluate(self, node=None):
        """🧮 Evaluate an expression tree containing integers and +,-,*,/."""
        if node is None:
            node = self.root
        if not node.is_operator():
            return int(node.value)
        left_val = self.evaluate(node.left)
        right_val = self.evaluate(node.right)
        if node.value == '+':
            return left_val + right_val
        elif node.value == '-':
            return left_val - right_val
        elif node.value == '*':
            return left_val * right_val
        elif node.value == '/':
            if right_val == 0:
                raise ValueError("Division by zero")
            return left_val // right_val  # Use // for integer division

# 🧪 Test cases
def test_evaluate_expression_tree():
    # Test 1: Leaf only
    tree = EvaluableExpressionTree()
    tree.root = Node("5")
    print("🌿 Test 1:", tree.evaluate() == 5)

    # Test 2: Addition
    tree = EvaluableExpressionTree()
    tree.build_from_postfix(["2", "3", "+"])
    print("➕ Test 2:", tree.evaluate() == 5)

    # Test 3: Mixed ops ((2+3)*4)
    tree = EvaluableExpressionTree()
    tree.build_from_postfix(["2", "3", "+", "4", "*"])
    print("🔁 Test 3:", tree.evaluate() == 20)

    # Test 4: Division (8/4)
    tree = EvaluableExpressionTree()
    tree.build_from_postfix(["8", "4", "/"])
    print("➗ Test 4:", tree.evaluate() == 2)

    # Test 5: Nested ((10+5)*2)-(8/4)
    tree = EvaluableExpressionTree()
    tree.build_from_postfix(["10", "5", "+", "2", "*", "8", "4", "/", "-"])
    print("🧠 Test 5:", tree.evaluate() == 28)

# 🚀 Run tests
test_evaluate_expression_tree()
