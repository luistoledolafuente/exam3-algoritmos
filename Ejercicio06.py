class ExprNode:
    """🌿 Nodo para árbol de expresiones"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self):
        self.root = None

    def build_from_postfix(self, postfix_tokens):
        """🔨 Construir árbol desde tokens en notación postfija"""
        stack = []
        operators = {"+", "-", "*", "/"}
        for token in postfix_tokens:
            node = ExprNode(token)
            if token in operators:
                node.right = stack.pop()
                node.left = stack.pop()
            stack.append(node)
        self.root = stack.pop() if stack else None


# 🧪 Casos de prueba
def test_build_from_postfix():
    tree = ExpressionTree()
    tree.build_from_postfix(["2", "3", "+"])
    cond1 = (tree.root and tree.root.value == "+" and 
             tree.root.left.value == "2" and tree.root.right.value == "3")
    print("➕ Test 1:", cond1)

    tree = ExpressionTree()
    tree.build_from_postfix(["2", "3", "4", "*", "+"])
    root = tree.root
    cond2 = (root and root.value == "+" and root.left.value == "2" and root.right.value == "*")
    print("📊 Test 2:", cond2)

    tree = ExpressionTree()
    tree.build_from_postfix(["1", "2", "+", "3", "4", "-", "*"])
    root = tree.root
    cond3 = (root and root.value == "*" and root.left.value == "+" and root.right.value == "-")
    print("🔄 Test 3:", cond3)

    tree = ExpressionTree()
    tree.build_from_postfix(["a", "b", "c", "*", "+"])
    root = tree.root
    cond4 = (root and root.value == "+" and root.left.value == "a" and root.right.value == "*")
    print("🔤 Test 4:", cond4)

    tree = ExpressionTree()
    tree.build_from_postfix(["x"])
    root = tree.root
    print("🌱 Test 5:", root and root.value == "x" and root.left is None and root.right is None)


# 🚀 Ejecutar tests
test_build_from_postfix()
