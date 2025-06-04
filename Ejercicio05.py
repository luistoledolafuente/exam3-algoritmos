class ExprNode:
    """🔢 Node for expression tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def is_operator(self):
        return self.value in ['+', '-', '*', '/']

class EvaluableExpressionTree:
    """🧮 Expression tree that can be evaluated with variables."""
    def __init__(self):
        super().__init__()  # Initializes self.root = None

    def evaluate_with_variables(self, variables):
        
        """
        🧮 Evaluate expression tree using provided `variables` dict.
        """
        def eval_node(node):
            if node is None:
                return 0
            # Si es operador, evaluamos recursivamente hijos
            if node.is_operator():
                left_val = eval_node(node.left)
                right_val = eval_node(node.right)
                if node.value == '+':
                    return left_val + right_val
                elif node.value == '-':
                    return left_val - right_val
                elif node.value == '*':
                    return left_val * right_val
                elif node.value == '/':
                    if right_val == 0:
                        raise ValueError("Division by zero!")
                    return left_val / right_val
            else:
                # Si no es operador, puede ser número o variable
                try:
                    return float(node.value)  # intenta convertir a número
                except ValueError:
                    # si no es número, debe estar en variables
                    if node.value in variables:
                        return float(variables[node.value])
                    else:
                        raise ValueError(f"Unknown variable: {node.value}")
        
        return eval_node(self.root)
        

# Helper to build a tree from postfix for tests
def build_expression_tree(postfix):
    stack = []
    ops = set(["+", "-", "*", "/"])
    for tok in postfix:
        node = ExprNode(tok)
        if tok in ops:
            node.right = stack.pop()
            node.left = stack.pop()
        stack.append(node)
    return stack.pop() if stack else None

# 🧪 Test cases
def test_evaluate_with_vars():
    tree = EvaluableExpressionTree()
    # Test 1: 2 3 +
    tree.root = build_expression_tree(["2", "3", "+"])
    print("🧪 Test 1:", tree.evaluate_with_variables({}) == 5.0)
    # Test 2: x 4 *
    tree.root = build_expression_tree(["x", "4", "*"])
    print("🧪 Test 2:", tree.evaluate_with_variables({"x": 2}) == 8.0)
    # Test 3: x y -
    tree.root = build_expression_tree(["x", "y", "-"])
    print("🧪 Test 3:", tree.evaluate_with_variables({"x": 5, "y": 3}) == 2.0)
    # Test 4: a b /
    tree.root = build_expression_tree(["a", "b", "/"])
    try:
        tree.evaluate_with_variables({"a": 8, "b": 0})
        print("🧪 Test 4: False")  # Should not reach here
    except ValueError as e:
        print("🧪 Test 4:", str(e) == "Division by zero!")
    # Test 5: x z +
    tree.root = build_expression_tree(["x", "z", "+"])
    try:
        tree.evaluate_with_variables({"x": 1})
        print("🧪 Test 5: False")  # Should not reach here
    except ValueError as e:
        print("🧪 Test 5:", str(e) == "Unknown variable: z")

# 🚀 Run tests
test_evaluate_with_vars()