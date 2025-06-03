class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self):
        self.root = None

class EvaluableExpressionTree(ExpressionTree):
    def __init__(self):
        super().__init__()

    def simplify(self, node=None):
        """
        🔄 Simplify constant-only subtrees into single numeric leaves.
        """
        if node is None:
            return None
        
        # Simplify children first
        node.left = self.simplify(node.left)
        node.right = self.simplify(node.right)

        # Check if node is operator with both children leaves that are digits
        if node.left and node.right:
            if node.left.left is None and node.left.right is None and node.left.value.isdigit() and \
               node.right.left is None and node.right.right is None and node.right.value.isdigit():
                
                left_val = int(node.left.value)
                right_val = int(node.right.value)
                if node.value == "+":
                    res = left_val + right_val
                elif node.value == "-":
                    res = left_val - right_val
                elif node.value == "*":
                    res = left_val * right_val
                elif node.value == "/":
                    # Integer division
                    res = left_val // right_val
                else:
                    return node
                
                # Return new leaf node with result
                return Node(str(res))

        # If no simplification possible, return the node itself
        return node


# Helper para tests (reutilizado)
def build_tree(postfix):
    stack = []
    ops = {"+", "-", "*", "/"}
    for tok in postfix:
        node = Node(tok)
        if tok in ops:
            node.right = stack.pop()
            node.left = stack.pop()
        stack.append(node)
    return stack.pop() if stack else None


# 🧪 Test cases
def test_simplify_expression_tree():
    et = EvaluableExpressionTree()

    # Test 1: All constants (2+3)
    et.root = build_tree(["2", "3", "+"])
    simp = et.simplify(et.root)
    print("🔢 Test 1:", simp and simp.value == "5" and simp.left is None and simp.right is None)

    # Test 2: Mixed (x+3)
    et.root = build_tree(["x", "3", "+"])
    simp = et.simplify(et.root)
    cond2 = (simp and simp.value == "+" and simp.left.value == "x" and simp.right.value == "3")
    print("🔤 Test 2:", cond2)

    # Test 3: Nested constants ((2*3)+(8-3))
    et.root = build_tree(["2", "3", "*", "8", "3", "-", "+"])
    simp = et.simplify(et.root)
    print("🎯 Test 3:", simp and simp.value == "11" and simp.left is None and simp.right is None)

    # Test 4: Partial ((2+3)*(z*4))
    et.root = build_tree(["2", "3", "+", "z", "4", "*", "*"])
    simp = et.simplify(et.root)
    cond4 = (simp and simp.value == "*" and simp.left.value == "5" and simp.right.value == "*")
    print("🔄 Test 4:", cond4)

    # Test 5: No simplify (x*y)
    et.root = build_tree(["x", "y", "*"])
    simp = et.simplify(et.root)
    print("🌿 Test 5:", simp and simp.value == "*" and simp.left.value == "x" and simp.right.value == "y")

# 🚀 Run tests
test_simplify_expression_tree()
