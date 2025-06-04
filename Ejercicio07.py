class Node:
    """🌿 Nodo para árbol de expresiones"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self):
        super().__init__()

    def build_from_postfix(self, postfix_tokens):
        stack = []
        operators = {"+", "-", "*", "/"}
        for token in postfix_tokens:
            node = Node(token)
            if token in operators:
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

        if node.left is None and node.right is None:
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
                raise ValueError("No se puede dividir entre el numero 0")
            return left_val / right_val

# Helper to build and test
def build_tree(postfix):
    stack = []
    ops = {"+", "-", "*", "/"}
    for tok in postfix:
        node = Node(tok)
        if tok in ops:
            node.right = stack.pop()
            node.left  = stack.pop()
        stack.append(node)
    return stack.pop() if stack else None

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