class GenericTreeNode:
    """Node for generic tree with multiple children."""
    def __init__(self, value):
        self.value = value
        self.children = []

    
    def add_child(self, value):
        """➕ Add a child node with the given value, return the new node."""
        new_node = GenericTreeNode(value)
        self.children.append(new_node)
        return new_node


# 🧪 Test cases
def test_add_child():
    root = GenericTreeNode("A")
    # Test 1
    child1 = root.add_child("B")
    print("🌳 Test 1:", root.children[0].value == "B")  # ✅
    # Test 2
    child2 = root.add_child("C")
    print("🌳 Test 2:", [c.value for c in root.children] == ["B", "C"])  # ✅
    # Test 3
    grandchild = child1.add_child("D")
    print("🌳 Test 3:", child1.children[0].value == "D")  # ✅
    # Test 4
    leaf_child = GenericTreeNode("X")
    new_grand = leaf_child.add_child("Y")
    print("🌳 Test 4:", leaf_child.children[0].value == "Y")  # ✅
    # Test 5
    root.add_child("E")
    print("🌳 Test 5:", [c.value for c in root.children] == ["B", "C", "E"])  # ✅

# 🚀 Run tests
test_add_child()
