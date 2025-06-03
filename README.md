# ✨ Midterm Exam: Trees & Advanced Trees Implementation 🌳🚀

This exam assesses your ability to implement core functionalities of **Generic Trees** and **Expression Trees** (Topic 9) in Python. You have **50 minutes** to solve all problems. Each implementation challenge includes automated test cases—each `print(True)` is worth **1 point**. Use only the provided method signatures, and adhere to best practices with descriptive variable names, clear comments, and ample emojis for engagement! 🎯🐍

---

## o1 Generic & Expression Trees 🛠️🌲

In this section, you will demonstrate your understanding of **Generic Trees** (multi-branch trees) and **Expression Trees** (binary trees for arithmetic expressions). Each of the 5 challenges below asks you to implement a specific method or function. Complete the method without changing its signature, and ensure all provided tests pass.

---

### 📌 🌳 Generic Tree Node Insertion

#### 🧩 Problem

Implement the method `add_child()` in the `GenericTreeNode` class to insert a new child node under a given parent.

#### 📜 Description

* You have a `GenericTreeNode` where each node holds a `value` and a list of `children`.
* Complete the `add_child(self, value)` method so that it:

  1. Creates a new `GenericTreeNode` with the given `value`.
  2. Appends it to `self.children`.
  3. Returns the newly created child node.
* Do **not** modify the constructor or other class definitions.
* Use this to build arbitrary multi-branch tree structures.

#### 🧪 5 Tests to Pass

1. Insert one child under a root; verify `root.children[0].value` matches.
2. Insert two children under the same parent; verify order and values.
3. Insert a child under a child node; verify grandchild relationship.
4. Call `add_child()` with a value on a leaf; verify children list of leaf is not empty.
5. Ensure multiple siblings keep correct parent–child relationships (no duplicates).

#### 🧩 Base Code

```python
class GenericTreeNode:
    """Node for generic tree with multiple children."""
    def __init__(self, value):
        self.value = value  # 📊 Data stored in node
        self.children = []  # 👶 List of child nodes
    
    def add_child(self, value):
        """➕ Add a child node with the given value, return the new node."""
        # Your solution here 🛠️
        pass

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
```

#### 💡 Tips

* Use `self.children.append(...)` to maintain sibling order.
* Always return the newly created node for chaining.
* Keep variable names descriptive (`new_node`, `child_node`, etc.).

#### 🧠 Motivation

Generic trees model real-world hierarchies (e.g., file systems, organizational charts). Mastering node insertion is key to dynamic tree construction and traversal tasks. 🌐📂

---

### 📌 🚶 Generic Tree Preorder Traversal

#### 🧩 Problem

Implement the `preorder_traversal()` method to return a list of node values in **preorder** (visit node, then children left-to-right).

#### 📜 Description

* Given a `GenericTree` class (which has `root` of type `GenericTreeNode`), implement `preorder_traversal(self, node=None, result=None)`.
* **If `node` or `result` is not provided**, default to starting at `self.root` and an empty list.
* Return a Python `list` of all `value` fields in preorder order.
* Must handle an empty tree (`self.root is None`) by returning `[]`.

#### 🧪 5 Tests to Pass

1. Single-node tree → returns `[root.value]`.
2. Two-level tree: root with two children → returns `[root, child1, child2]`.
3. Three-level tree with varying numbers of children → correct nested preorder list.
4. Empty tree (`root = None`) → returns `[]`.
5. Tree with multiple children and grandchildren → all values appear exactly once in correct order.

#### 🧩 Base Code

```python
class GenericTree:
    """Generic tree implementation with basic operations."""
    def __init__(self):
        self.root = None  # 🌱 Root of the tree

    def preorder_traversal(self, node=None, result=None):
        """
        📝 Visit node first, then all children (DLR).
        Returns a list of values in preorder.
        """
        # Your solution here 🛠️
        pass

# 🧪 Test cases
def test_generic_preorder():
    tree = GenericTree()
    # Test 1: Empty tree
    print("🚶 Test 1:", tree.preorder_traversal() == [])  # 📭
    # Construct tree:
    #      A
    #    / | \
    #   B  C  D
    #      |
    #      E
    tree.root = GenericTreeNode("A")
    b = tree.root.add_child("B")
    c = tree.root.add_child("C")
    d = tree.root.add_child("D")
    c.add_child("E")
    # Test 2
    print("🚶 Test 2:", tree.preorder_traversal() == ["A", "B", "C", "E", "D"])  # ✅
    # Test 3: Single node after resetting
    single = GenericTree()
    single.root = GenericTreeNode(42)
    print("🚶 Test 3:", single.preorder_traversal() == [42])  # 🌱
    # Test 4: More complex
    c.add_child("F")
    b.add_child("G")
    print("🚶 Test 4:", tree.preorder_traversal() == ["A", "B", "G", "C", "E", "F", "D"])  # 🔁
    # Test 5: Verify no duplication
    values = tree.preorder_traversal()
    print("🚶 Test 5:", len(values) == len(set(values)))  # 📏 Unique

# 🚀 Run tests
test_generic_preorder()
```

#### 💡 Tips

* Use recursion: append `node.value`, then loop over `node.children`.
* Guard against `node is None` to return `result` immediately.
* Initialize `result` once at start: `if result is None: result = []`.

#### 🧠 Motivation

Preorder traversal is used in tasks like **serializing** hierarchical data (e.g., saving a folder structure). Understanding how to traverse generic trees prepares you for more advanced tree algorithms. 🌿🔄

---

### 📌 🌳 Expression Tree Build from Prefix

#### 🧩 Problem

Implement `build_from_prefix()` to construct an **ExpressionTree** from a list of prefix tokens.

#### 📜 Description

* Given a list of tokens (strings) representing a **prefix** (Polish) expression (e.g., `["*", "+", "2", "3", "4"]`), build the corresponding binary expression tree.
* Operators are one of `{"+", "-", "*", "/"}`; operands are alphanumeric (e.g., `"2"`, `"x"`).
* **Algorithm**:

  1. Process tokens in **reverse order**.
  2. For each token, if it’s an operand, create a `Node(token)` and push onto a stack.
  3. If it’s an operator, pop two nodes (`left`, then `right`), create `Node(operator)` with those children, push the new node back.
  4. After processing all tokens, remaining stack item is `self.root`.
* Do **not** modify the `ExpressionTree` constructor or `Node` class.

#### 🧪 5 Tests to Pass

1. Prefix `["+", "2", "3"]` → root `"+"`, left `"2"`, right `"3"`.
2. Prefix `["*", "+", "1", "2", "3"]` → matches `(1+2)*3` structure.
3. Prefix with variables: `["-", "x", "y"]` → root `"-"`, children `"x"`, `"y"`.
4. Longer prefix: `["-", "*", "2", "3", "/", "8", "4"]` → structure `((2*3) - (8/4))`.
5. Empty or invalid prefix list → handle gracefully by leaving `self.root = None`.

#### 🧩 Base Code

```python
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
        # Your solution here 🛠️
        pass

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
```

#### 💡 Tips

* Process the `prefix_tokens` in **reverse** order for the standard stack algorithm.
* Always check for empty list to avoid index errors.
* Use a Python list as a stack: `stack.append(...)` and `stack.pop()`.

#### 🧠 Motivation

Building from prefix equips you to parse expressions in many compilers and calculators. Understanding both prefix and postfix builds deepens your grasp of parsing techniques. 🧮🔣

---

### 📌 📝 Expression Tree Inorder Conversion

#### 🧩 Problem

Implement `infix_traversal()` to produce the **infix** (human-readable) notation string from an **ExpressionTree**, adding parentheses to reflect proper precedence.

#### 📜 Description

* Given an `ExpressionTree` with internal operator nodes and leaf operand nodes, implement `infix_traversal(self, node=None)`.
* If `node` is `None`, start at `self.root`.
* Return a **string** representing the infix expression, with parentheses around every operator subtree.
* Leaves (operands) should return their value without parentheses.
* Example: For a tree representing `(2 + 3) * 4`, return `"((2 + 3) * 4)"`.

#### 🧪 5 Tests to Pass

1. Single-operand tree → returns `"42"`.
2. Simple binary: `["+", "2", "3"]` → returns `"(2 + 3)"`.
3. Nested: `["*", "+", "2", "3", "4"]` → returns `"((2 + 3) * 4)"`.
4. More complex: `["-", "*", "1", "2", "/", "8", "4"]` → returns `"((1 * 2) - (8 / 4))"`.
5. Empty tree (`root = None`) → returns `""` (empty string).

#### 🧩 Base Code

```python
class Node:
    """Node for expression tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def is_operator(self):
        return self.value in ['+', '-', '*', '/']

class ExpressionTree:
    """Expression tree with traversal operations."""
    def __init__(self):
        self.root = None  # 🌱 Root of expression tree

    def infix_traversal(self, node=None):
        """
        📝 Return a string of the infix expression with parentheses.
        """
        # Your solution here 🛠️
        pass

# 🧪 Test cases
def test_infix_traversal():
    tree = ExpressionTree()
    # Test 1: Empty tree
    print("📝 Test 1:", tree.infix_traversal() == "")  # 📭
    # Build simple (2 + 3)
    root = Node("+")
    root.left = Node("2")
    root.right = Node("3")
    tree.root = root
    print("📝 Test 2:", tree.infix_traversal() == "(2 + 3)")  # ✅
    # Build ((2+3)*4)
    root = Node("*")
    left = Node("+"); left.left = Node("2"); left.right = Node("3")
    root.left = left; root.right = Node("4")
    tree.root = root
    print("📝 Test 3:", tree.infix_traversal() == "((2 + 3) * 4)")  # ✅
    # Build ((1*2) - (8/4))
    root = Node("-")
    l = Node("*"); l.left = Node("1"); l.right = Node("2")
    r = Node("/"); r.left = Node("8"); r.right = Node("4")
    root.left = l; root.right = r
    tree.root = root
    print("📝 Test 4:", tree.infix_traversal() == "((1 * 2) - (8 / 4))")  # ✅
    # Test 5: Single operand
    tree.root = Node("X")
    print("📝 Test 5:", tree.infix_traversal() == "X")  # 🌱

# 🚀 Run tests
test_infix_traversal()
```

#### 💡 Tips

* Check `if node is None` early to return `""`.
* If `not node.is_operator()`, return `node.value`.
* Otherwise, recursively build `left_str = infix_traversal(node.left)`, `right_str = infix_traversal(node.right)`, then return `f"({left_str} {node.value} {right_str})"`.

#### 🧠 Motivation

Infix conversion with parentheses is crucial in compilers and expression evaluators to preserve operator precedence. You’ll see this in language interpreters and calculators. 📚🔣

---

### 📌 🧪 Expression Tree Evaluation with Variables

#### 🧩 Problem

Implement `evaluate_with_variables(variables)` to compute the numeric result of an expression tree containing both numbers and variable names, given a dictionary mapping variables to numeric values.

#### 📜 Description

* Given an `ExpressionTree` whose leaves are either numeric strings (e.g., `"5"`) or variable names (e.g., `"x"`), implement:

  ```python
  def evaluate_with_variables(self, variables):
      """
      Evaluate the expression tree using the provided dictionary `variables`.
      """
  ```
* If a leaf’s `value` is in `variables`, use `variables[value]` (a float or int).
* Otherwise, attempt to convert to `float(value)`; if that fails, raise `ValueError("Unknown variable: {value}")`.
* Handle `+`, `-`, `*`, `/` operators; division by zero should raise `ValueError("Division by zero!")`.
* Return a Python `float` for the final result.

#### 🧪 5 Tests to Pass

1. Tree `"2 + 3"` with empty variables → returns `5.0`.
2. Tree `["*", "x", "4"]` with `{"x": 2}` → returns `8.0`.
3. Tree `["-", "x", "y"]` with `{"x": 5, "y": 3}` → returns `2.0`.
4. Tree `["/", "a", "b"]` with `{"a": 8, "b": 0}` → raises `ValueError("Division by zero!")`.
5. Tree `["+", "x", "z"]` with `{"x": 1}` → raises `ValueError("Unknown variable: z")`.

#### 🧩 Base Code

```python
class Node:
    """Node for expression tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def is_operator(self):
        return self.value in ['+', '-', '*', '/']

class EvaluableExpressionTree:
    """Expression tree that can be evaluated with variables."""
    def __init__(self):
        self.root = None  # 🌱 Root of expression tree

    def evaluate_with_variables(self, variables):
        """
        🧮 Evaluate expression tree using provided `variables` dict.
        """
        # Your solution here 🛠️
        pass

# Helper to build a tree from postfix for tests
def build_expression_tree(postfix):
    stack = []
    ops = set(["+", "-", "*", "/"])
    for tok in postfix:
        node = Node(tok)
        if tok in ops:
            node.right = stack.pop()
            node.left = stack.pop()
        stack.append(node)
    return stack.pop() if stack else None

# 🧪 Test cases
def test_evaluate_with_vars():
    tree = EvaluableExpressionTree()
    # Test 1
    tree.root = build_expression_tree(["2", "3", "+"])
    print("🧪 Test 1:", tree.evaluate_with_variables({}) == 5.0)  # ✅
    # Test 2
    tree.root = build_expression_tree(["x", "4", "*"])
    print("🧪 Test 2:", tree.evaluate_with_variables({"x": 2}) == 8.0)  # ✅
    # Test 3
    tree.root = build_expression_tree(["x", "y", "-"])
    print("🧪 Test 3:", tree.evaluate_with_variables({"x": 5, "y": 3}) == 2.0)  # ✅
    # Test 4
    tree.root = build_expression_tree(["a", "b", "/"])
    try:
        tree.evaluate_with_variables({"a": 8, "b": 0})
        print("🧪 Test 4: False")  # Should not reach here
    except ValueError as e:
        print("🧪 Test 4:", str(e) == "Division by zero!")  # ⚠️
    # Test 5
    tree.root = build_expression_tree(["x", "z", "+"])
    try:
        tree.evaluate_with_variables({"x": 1})
        print("🧪 Test 5: False")  # Should not reach here
    except ValueError as e:
        print("🧪 Test 5:", str(e) == "Unknown variable: z")  # ❌

# 🚀 Run tests
test_evaluate_with_vars()
```

#### 💡 Tips

* Base case: if `node is None`, return `0.0`.
* If `not node.is_operator()`:

  * If `node.value in variables`, return `float(variables[node.value])`.
  * Else try `float(node.value)` or raise `ValueError`.
* For operators, recursively evaluate left/right, then apply operator; guard against division by zero.

#### 🧠 Motivation

Evaluating expressions with variables is a cornerstone of **interpreters**, **symbolic math packages**, and **data analysis pipelines**. You’ll build on these skills in compiler design and scientific computing. 🧙‍♂️📊

---

## o2 Expression Trees (Parsing & Evaluation) 🛠️🌲

In this section, you will implement core functions to build, traverse, evaluate, and simplify expression trees. 

---

### 🧩 Build Expression Tree from Postfix

#### ❓ Problem

Implement `build_expression_tree(postfix_tokens)` to convert a postfix token list into an expression tree.

#### 📜 Description

* Given a list of tokens in **postfix** order (e.g., `["2", "3", "4", "*", "+"]`), build a binary tree where each internal node is an operator (`"+", "-", "*", "/"`) and each leaf is an operand (numeric or variable string).
* Use a stack-based algorithm:

  1. Initialize an empty stack.
  2. For each token in `postfix_tokens`:

     * If it’s not an operator, create a new `Node(token)` and push onto the stack.
     * If it’s an operator, pop the top two nodes (`right`, then `left`), create a `Node(operator)` with `left` and `right` as children, then push the new node.
  3. After processing all tokens, the stack’s sole element is the root.
* Do **not** modify the `Node` class.

#### 🧪 5 Tests to Pass

1. **Simple addition**: Input `["2", "3", "+"]` → root `"+"`, left `"2"`, right `"3"`.
2. **Operator precedence**: Input `["2", "3", "4", "*", "+"]` → matches `(2 + (3*4))`.
3. **Nested operations**: Input `["1", "2", "+", "3", "4", "-", "*"]` → tree `((1+2)*(3-4))`.
4. **Variables**: Input `["a", "b", "c", "*", "+"]` → tree `(a + (b*c))`.
5. **Single operand**: Input `["x"]` → root `"x"` with no children.

#### 🧩 Base Code

```python
class Node:
    """Node for expression tree."""
    def __init__(self, value):
        self.value = value        # Operator or operand (string)
        self.left = None          # Left child (Node or None)
        self.right = None         # Right child (Node or None)

def build_expression_tree(postfix_tokens):
    """🔨 Build expression tree from postfix notation using a stack."""
    # Your solution here 🛠️
    pass

# 🧪 Test cases
def test_build_expression_tree():
    # Test 1: Simple addition
    root = build_expression_tree(["2", "3", "+"])
    print("➕ Test 1:", root.value == "+" and root.left.value == "2" and root.right.value == "3")
    # Test 2: Operator precedence
    root = build_expression_tree(["2", "3", "4", "*", "+"])
    cond2 = (root.value == "+" and root.left.value == "2" and root.right.value == "*")
    print("📊 Test 2:", cond2)
    # Test 3: Nested operations
    root = build_expression_tree(["1", "2", "+", "3", "4", "-", "*"])
    cond3 = (root.value == "*" and root.left.value == "+" and root.right.value == "-")
    print("🔄 Test 3:", cond3)
    # Test 4: Variables
    root = build_expression_tree(["a", "b", "c", "*", "+"])
    cond4 = (root.value == "+" and root.left.value == "a" and root.right.value == "*")
    print("🔤 Test 4:", cond4)
    # Test 5: Single operand
    root = build_expression_tree(["x"])
    print("🌱 Test 5:", root.value == "x" and root.left is None and root.right is None)

# 🚀 Run tests
test_build_expression_tree()
```

#### 💡 Tips

* Use a Python list as a stack: `stack = []`, `stack.append(...)`, `stack.pop()`.
* Check membership in `operators = {"+", "-", "*", "/"}` for each token.
* Handle the single-token case by returning that node immediately.

#### 🧠 Motivation

Building from postfix is fundamental in compilers and calculators. It leverages stack discipline to parse expressions efficiently.

---

### 🧩 Evaluate Expression Tree

#### ❓ Problem

Implement `evaluate_expression_tree(root)` to compute the integer result of an expression tree containing only integer operands and operators `+`, `-`, `*`, `/`.

#### 📜 Description

* Given the `root` of an expression tree, compute its value via **post-order traversal**:

  1. If `root` is `None`, return `0`.
  2. If `root` is a leaf (no children), return `int(root.value)`.
  3. Otherwise, recursively evaluate `left_val = evaluate_expression_tree(root.left)` and `right_val = evaluate_expression_tree(root.right)`.
  4. Apply `root.value`:

     * `"+"`: return `left_val + right_val`
     * `"-"`: return `left_val - right_val`
     * `"*"`: return `left_val * right_val`
     * `"/"`: return `left_val // right_val` (integer division)
     * Otherwise, raise `ValueError(f"Unsupported operator: {root.value}")`.

#### 🧪 5 Tests to Pass

1. **Leaf only**: Tree `Node("5")` → returns `5`.
2. **Addition**: Tree for `2 + 3` → returns `5`.
3. **Mixed ops**: Tree representing `(2 + 3) * 4` → returns `20`.
4. **Division**: Tree representing `8 / 4` → returns `2`.
5. **Nested**: Tree representing `((10 + 5) * 2) - (8 / 4)` → returns `28`.

#### 🧩 Base Code

```python
def evaluate_expression_tree(root):
    """🧮 Evaluate an expression tree containing integers and +, -, *, /."""
    # Your solution here 🛠️
    pass

# Helper: Build from postfix for tests
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
def test_evaluate_expression_tree():
    # Test 1: Leaf only
    root = Node("5")
    print("🌿 Test 1:", evaluate_expression_tree(root) == 5)
    # Test 2: Addition (2 + 3)
    root = build_tree(["2", "3", "+"])
    print("➕ Test 2:", evaluate_expression_tree(root) == 5)
    # Test 3: Mixed ops ((2+3)*4)
    root = build_tree(["2", "3", "+", "4", "*"])
    print("🔁 Test 3:", evaluate_expression_tree(root) == 20)
    # Test 4: Division (8/4)
    root = build_tree(["8", "4", "/"])
    print("➗ Test 4:", evaluate_expression_tree(root) == 2)
    # Test 5: Nested ((10+5)*2)-(8/4)
    root = build_tree(["10", "5", "+", "2", "*", "8", "4", "/", "-"])
    print("🧠 Test 5:", evaluate_expression_tree(root) == 28)

# 🚀 Run tests
test_evaluate_expression_tree()
```

#### 💡 Tips

* Use `if not root:` to handle `None`.
* Detect leaf by `if root.left is None and root.right is None:`.
* Carefully use `//` for integer division to match test expectations.

#### 🧠 Motivation

Evaluating expression trees underpins many arithmetic interpreters and query engines, enabling efficient computation without string parsing each time.

---

### 🧩 Inorder, Preorder, and Postorder Traversals

#### ❓ Problem

Implement three traversal functions—`inorder_traversal(root, result_list)`, `preorder_traversal(root, result_list)`, and `postorder_traversal(root, result_list)`—to produce **infix**, **prefix**, and **postfix** notation lists, respectively.

#### 📜 Description

* **Inorder** (`left, root, right`): Append `"("` before left recursion if `root.value` is an operator, then `root.value`, then `")"` after right recursion.
* **Preorder** (`root, left, right`): Append `root.value` first, then traverse left, then traverse right.
* **Postorder** (`left, right, root`): Traverse left, traverse right, then append `root.value`.
* All functions should guard `if root is None: return`.
* `result_list` is a Python list passed by reference to accumulate tokens.

#### 🧪 5 Tests to Pass

1. **Simple tree**: `(2 + 3)` → Inorder: `["(", "2", "+", "3", ")"]`; Preorder: `["+", "2", "3"]`; Postorder: `["2", "3", "+"]`.
2. **Nested**: `((2 + 3) * (4 - 1))` → Inorder: `["(", "(", "2", "+", "3", ")", "*", "(", "4", "-", "1", ")", ")"]`; Preorder: `["*", "+", "2", "3", "-", "4", "1"]`; Postorder: `["2", "3", "+", "4", "1", "-", "*"]`.
3. **Single node**: `"X"` → Inorder: `["X"]`; Preorder: `["X"]`; Postorder: `["X"]`.
4. **Empty tree**: `root = None` → all traversals return `[]`.
5. **Mixed operators**: `(1 * (2 + 3))` → correct sequences with parentheses.

#### 🧩 Base Code

```python
def inorder_traversal(root, result_list):
    """
    📝 Inorder traversal (left, root, right) to generate infix notation.
    Use parentheses for operators.
    """
    # Your solution here 🛠️
    pass

def preorder_traversal(root, result_list):
    """🚀 Preorder traversal (root, left, right) to generate prefix notation."""
    # Your solution here 🛠️
    pass

def postorder_traversal(root, result_list):
    """🧠 Postorder traversal (left, right, root) to generate postfix notation."""
    # Your solution here 🛠️
    pass

# Helper: Build from postfix for tests
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
def test_traversals():
    # Build tree for ((2+3)*(4-1))
    root = build_tree(["2", "3", "+", "4", "1", "-", "*"])
    # Test 1
    infix = []; inorder_traversal(root, infix)
    print("📝 Test 1 (Infix):", "".join(infix) == "((2+3)*(4-1))")
    prefix = []; preorder_traversal(root, prefix)
    print("🚀 Test 1 (Prefix):", " ".join(prefix) == "* + 2 3 - 4 1")
    postfix = []; postorder_traversal(root, postfix)
    print("🧠 Test 1 (Postfix):", " ".join(postfix) == "2 3 + 4 1 - *")
    # Test 2: Single node "X"
    single = Node("X")
    infix2 = []; inorder_traversal(single, infix2)
    print("🌱 Test 2 (Infix):", infix2 == ["X"])
    prefix2 = []; preorder_traversal(single, prefix2)
    print("🌱 Test 2 (Prefix):", prefix2 == ["X"])
    postfix2 = []; postorder_traversal(single, postfix2)
    print("🌱 Test 2 (Postfix):", postfix2 == ["X"])
    # Test 3: Empty tree
    inf3 = []; inorder_traversal(None, inf3)
    print("📭 Test 3 (Infix):", inf3 == [])
    pre3 = []; preorder_traversal(None, pre3)
    print("📭 Test 3 (Prefix):", pre3 == [])
    post3 = []; postorder_traversal(None, post3)
    print("📭 Test 3 (Postfix):", post3 == [])
    # Test 4: (1 * (2 + 3))
    root2 = build_tree(["1", "2", "3", "+", "*"])
    inf4 = []; inorder_traversal(root2, inf4)
    print("🔄 Test 4 (Infix):", "".join(inf4) == "(1*(2+3))")
    pre4 = []; preorder_traversal(root2, pre4)
    print("🔄 Test 4 (Prefix):", " ".join(pre4) == "* 1 + 2 3")
    post4 = []; postorder_traversal(root2, post4)
    print("🔄 Test 4 (Postfix):", " ".join(post4) == "1 2 3 + *")

# 🚀 Run tests
test_traversals()
```

#### 💡 Tips

* For **inorder**: check if `root.value` is an operator via `if root.value in {"+","-","*","/"}`, then add `"("` before descending left and `")"` after descending right.
* For **preorder** and **postorder**, simply append before/after recursing.
* Always guard with `if root is None: return`.

#### 🧠 Motivation

Traversal methods connect tree structures to expression notations (infix, prefix, postfix). They’re core to parsing and generating code or evaluating expressions.

---

### 🧩 Infix to Postfix Conversion

#### ❓ Problem

Implement `infix_to_postfix(tokens)` to convert a list of **infix** tokens to **postfix** tokens using a stack-based algorithm.

#### 📜 Description

* `tokens` is a list of strings representing an infix expression, including:

  * Operands: alphanumeric (e.g., `"2"`, `"x"`)
  * Operators: `"+", "-", "*", "/"`
  * Parentheses: `"("`, `")"`
* Use the **shunting-yard**–style approach:

  1. Initialize empty `output` list and empty `stack`.
  2. For each `token` in `tokens`:

     * If `token.isalnum()`, append to `output`.
     * If `token == "("`, push to `stack`.
     * If `token == ")"`, pop from `stack` to `output` until `"("` is encountered (pop and discard `"("`).
     * If `token` is an operator, pop from `stack` to `output` while top of `stack` is operator with **≥** precedence. Then push `token`.
  3. After processing, pop any remaining operators from `stack` to `output`.
* Return the `output` list.

#### 🧪 5 Tests to Pass

1. **Simple**: `["2", "+", "3"]` → `["2", "3", "+"]`.
2. **Precedence**: `["2", "+", "3", "*", "4"]` → `["2", "3", "4", "*", "+"]`.
3. **Parentheses**: `["(", "2", "+", "3", ")", "*", "4"]` → `["2", "3", "+", "4", "*"]`.
4. **Complex**: `["(", "1", "+", "2", ")", "*", "(", "3", "-", "4", ")"]` → `["1", "2", "+", "3", "4", "-", "*"]`.
5. **Multiple operators**: `["a", "+", "b", "*", "c", "/", "d"]` → `["a", "b", "c", "*", "d", "/", "+"]`.

#### 🧩 Base Code

```python
def infix_to_postfix(tokens):
    """
    📜 Convert a list of infix tokens to postfix notation.
    """
    # Your solution here 🛠️
    pass

# 🧪 Test cases
def test_infix_to_postfix():
    # Test 1: Simple
    print("➕ Test 1:", infix_to_postfix(["2", "+", "3"]) == ["2", "3", "+"])
    # Test 2: Precedence
    print("📊 Test 2:", infix_to_postfix(["2", "+", "3", "*", "4"]) == ["2", "3", "4", "*", "+"])
    # Test 3: Parentheses
    print("🔗 Test 3:", infix_to_postfix(["(", "2", "+", "3", ")", "*", "4"]) == ["2", "3", "+", "4", "*"])
    # Test 4: Complex
    print("🧮 Test 4:", infix_to_postfix(["(", "1", "+", "2", ")", "*", "(", "3", "-", "4", ")"]) ==
          ["1", "2", "+", "3", "4", "-", "*"])
    # Test 5: Variables
    print("🔤 Test 5:", infix_to_postfix(["a", "+", "b", "*", "c", "/", "d"]) == ["a", "b", "c", "*", "d", "/", "+"])

# 🚀 Run tests
test_infix_to_postfix()
```

#### 💡 Tips

* Maintain a **precedence** dictionary: `precedence = {"+":1, "-":1, "*":2, "/":2}`.
* Use `token.isalnum()` to detect operands.
* When popping operators, check `while stack and stack[-1] in precedence and precedence[stack[-1]] >= precedence[token]`.

#### 🧠 Motivation

Converting infix to postfix is a classic compiler task. Postfix is easier to evaluate and build into trees.

---

### 🧩 Simplify Expression Tree

#### ❓ Problem

Implement `simplify_expression_tree(root)` to collapse any constant-only subtrees into single numeric leaves.

#### 📜 Description

* Given `root` of an expression tree where some subtrees contain **only integer leaves**, replace each such subtree by a new leaf whose `value` is the computed integer.
* Steps:

  1. If `root` is `None`, return `None`.
  2. Recursively call `simplify_expression_tree` on `root.left` and `root.right`.
  3. After recursion, if both `root.left` and `root.right` are leaves **and** their `value` strings are numeric (use `int(...)`), compute the integer result for `root.value` operator (`+`, `-`, `*`, `//`).
  4. Create a new `Node(str(computed))` and return it instead of the original subtree.
  5. Otherwise, return `root` (with possibly simplified children).

#### 🧪 5 Tests to Pass

1. **All constants**: Tree `(2 + 3)` → simplified root `"5"` with no children.
2. **Mixed**: Tree `(x + 3)` → remains unchanged.
3. **Nested constants**: Tree `((2 * 3) + (8 - 3))` → entire tree becomes `"11"`.
4. **Partial**: Tree `((2 + 3) * (z * 4))` → left collapses to `"5"`, right remains subtree `(z*4)`.
5. **No simplification needed**: Tree `(x * y)` → remains as is.

#### 🧩 Base Code

```python
def simplify_expression_tree(root):
    """
    🔄 Simplify an expression tree by evaluating constant-only subtrees.
    Returns a possibly new root with constants collapsed.
    """
    # Your solution here 🛠️
    pass

# Helper: Build from postfix for tests
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
    # Test 1: All constants (2+3)
    root = build_tree(["2", "3", "+"])
    simp = simplify_expression_tree(root)
    print("🔢 Test 1:", simp.value == "5" and simp.left is None and simp.right is None)
    # Test 2: Mixed (x+3)
    root = build_tree(["x", "3", "+"])
    simp = simplify_expression_tree(root)
    cond2 = (simp.value == "+" and simp.left.value == "x" and simp.right.value == "3")
    print("🔤 Test 2:", cond2)
    # Test 3: Nested constants ((2*3)+(8-3))
    root = build_tree(["2", "3", "*", "8", "3", "-", "+"])
    simp = simplify_expression_tree(root)
    print("🎯 Test 3:", simp.value == "11" and simp.left is None and simp.right is None)
    # Test 4: Partial ((2+3)*(z*4))
    root = build_tree(["2", "3", "+", "z", "4", "*", "*"])
    simp = simplify_expression_tree(root)
    cond4 = (simp.value == "*" and simp.left.value == "5" and simp.right.value == "*")
    print("🔄 Test 4:", cond4)
    # Test 5: No simplification needed (x*y)
    root = build_tree(["x", "y", "*"])
    simp = simplify_expression_tree(root)
    print("🌿 Test 5:", simp.value == "*" and simp.left.value == "x" and simp.right.value == "y")

# 🚀 Run tests
test_simplify_expression_tree()
```

#### 💡 Tips

* Determine **leaf** by `if not root.left and not root.right`.
* Use `try: left_val = int(root.left.value) ...` to test numeric.
* After computing, return a **new** `Node(str(computed))` to replace the entire subtree.

#### 🧠 Motivation

Simplification optimizes expression evaluation and generates clearer output; critical in symbolic math systems and compilers.

---

## o3 Binary Search Trees (BST) & Search 🛠️🌲

In this section, you will implement core operations on a BST: inserting values, searching for values, building the tree from a list, traversing in-order, and finding the minimum key.

---

### 🧩 Insert Value into BST

#### ❓ Problem

Implement the method `insert(self, value)` in class `BinarySearchTree` to add a new integer into the BST, preserving the BST property.

#### 📜 Description

* You have a class `Node` with attributes `value` (int), `left`, and `right`.
* You have a class `BinarySearchTree` with an attribute `root` initially set to `None`.
* Implement `insert(self, value)` so that:

  1. If `self.root` is `None`, create `Node(value)` and set it as `self.root`.
  2. Otherwise, call a helper `_insert(node, value)` starting at `self.root`.
* `_insert(node, value)` must:

  * If `value < node.value` and `node.left` is `None`, assign `node.left = Node(value)`.
  * If `value < node.value` and `node.left` exists, recurse to `_insert(node.left, value)`.
  * If `value >= node.value` and `node.right` is `None`, assign `node.right = Node(value)`.
  * If `value >= node.value` and `node.right` exists, recurse to `_insert(node.right, value)`.
* Do not modify the class signature.

#### 🧪 5 Tests to Pass

1. **Insert into empty**: Create `bst = BinarySearchTree()`, call `bst.insert(10)`, then `bst.root.value == 10`.
2. **Left child**: Insert `[10, 5]` → `bst.root.left.value == 5`.
3. **Right child**: Insert `[10, 15]` → `bst.root.right.value == 15`.
4. **Deep insert**: Insert `[10, 5, 15, 3, 7]` → verify `bst.root.left.left.value == 3` and `bst.root.left.right.value == 7`.
5. **Duplicates to right**: Insert `[10, 10]` → second `10` should go to `bst.root.right.value == 10`.

#### 🧩 Base Code

```python
class Node:
    """🌱 Node for Binary Search Tree"""
    def __init__(self, value):
        self.value = value   # 🔢 Node value (int)
        self.left = None     # 🌿 Left child (Node or None)
        self.right = None    # 🌿 Right child (Node or None)

class BinarySearchTree:
    """🌳 BST with insert functionality (incomplete)."""
    def __init__(self):
        self.root = None  # 📭 Initially empty

    def insert(self, value):
        """🧩 Insert a value into the BST."""
        # Your solution here 🛠️
        pass

    def _insert(self, node, value):
        """🔄 Recursive helper for insert."""
        # Your solution here 🛠️
        pass

# 🧪 Test cases
def test_insert():
    # Test 1: Insert into empty
    bst = BinarySearchTree()
    bst.insert(10)
    print("🌱 Test 1:", bst.root is not None and bst.root.value == 10)
    # Test 2: Left child
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    print("👈 Test 2:", bst.root.left is not None and bst.root.left.value == 5)
    # Test 3: Right child
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(15)
    print("👉 Test 3:", bst.root.right is not None and bst.root.right.value == 15)
    # Test 4: Deep insert
    bst = BinarySearchTree()
    for v in [10, 5, 15, 3, 7]:
        bst.insert(v)
    cond4 = (bst.root.left.left.value == 3 and bst.root.left.right.value == 7)
    print("🔄 Test 4:", cond4)
    # Test 5: Duplicates to right
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(10)
    print("🔁 Test 5:", bst.root.right is not None and bst.root.right.value == 10)

# 🚀 Run tests
test_insert()
```

#### 💡 Tips

* Always compare `value` with `node.value`.
* For `value >= node.value`, send duplicates to the **right**.
* Use recursion to traverse until you find a `None` child.

#### 🧠 Motivation

Insertion is fundamental: it shapes the BST structure, determining search performance. Mastering this underpins many search-related algorithms.

---

### 🧩 Search Value in BST

#### ❓ Problem

Implement `search(self, value)` in class `BinarySearchTree` to return `True` if the integer `value` exists in the tree, else return `False`.

#### 📜 Description

* Given an integer `value`, start at `self.root`.
* If `node` is `None`, return `False`.
* If `node.value == value`, return `True`.
* If `value < node.value`, recurse into `node.left`.
* Otherwise, recurse into `node.right`.
* Provide a helper `_search(node, value)` to perform recursion; `search()` simply calls `_search(self.root, value)`.

#### 🧪 5 Tests to Pass

1. **Empty tree**: `bst = BinarySearchTree()` → `bst.search(5)` returns `False`.
2. **Root exists**: Insert `10`, then `bst.search(10)` returns `True`.
3. **Left subtree**: Insert `[10, 5, 3]`, then `bst.search(3)` returns `True`.
4. **Right subtree**: Insert `[10, 5, 15, 20]`, then `bst.search(20)` returns `True`.
5. **Not found**: Insert `[10, 5, 15]`, then `bst.search(7)` returns `False`.

#### 🧩 Base Code

```python
class BinarySearchTree(BinarySearchTree):
    def search(self, value):
        """🔍 Return True if value exists in BST, else False."""
        # Your solution here 🛠️
        pass

    def _search(self, node, value):
        """🔁 Recursive search helper."""
        # Your solution here 🛠️
        pass

# 🧪 Test cases
def test_search():
    # Test 1: Empty tree
    bst = BinarySearchTree()
    print("📭 Test 1:", bst.search(5) == False)
    # Test 2: Root exists
    bst = BinarySearchTree()
    bst.insert(10)
    print("🎯 Test 2:", bst.search(10) == True)
    # Test 3: Left subtree
    bst = BinarySearchTree()
    for v in [10, 5, 3]:
        bst.insert(v)
    print("‍👈 Test 3:", bst.search(3) == True)
    # Test 4: Right subtree
    bst = BinarySearchTree()
    for v in [10, 5, 15, 20]:
        bst.insert(v)
    print("👉 Test 4:", bst.search(20) == True)
    # Test 5: Not found
    bst = BinarySearchTree()
    for v in [10, 5, 15]:
        bst.insert(v)
    print("❌ Test 5:", bst.search(7) == False)

# 🚀 Run tests
test_search()
```

#### 💡 Tips

* Base case: if `node is None`, return `False`.
* Compare `value` with `node.value` and move left or right accordingly.
* Return immediately when found.

#### 🧠 Motivation

Searching leverages BST structure to achieve **O(log n)** on average, foundational for fast lookups and dictionary-like data.

---

### 🧩 Build BST from List of Values

#### ❓ Problem

Implement `build_from_list(self, values)` in `BinarySearchTree` to insert multiple integers in sequence.

#### 📜 Description

* `values` is a Python list of integers.
* For each integer in `values`, call `self.insert(val)`.
* After completion, `self.root` should represent the BST containing all inserted values.
* Guarantee that duplicates are still inserted to the right.

#### 🧪 5 Tests to Pass

1. **Empty list**: `bst = BinarySearchTree(); bst.build_from_list([])` → `bst.root is None`.
2. **Single element**: `[5]` → `bst.root.value == 5`.
3. **Multiple Insert**: `[10, 5, 15]` → verify `bst.root.left.value == 5` and `bst.root.right.value == 15`.
4. **Duplicates**: `[10, 10, 10]` → chain to the right: `root.value == 10`, `root.right.value == 10`, `root.right.right.value == 10`.
5. **Unsorted order**: `[7, 3, 11, 1, 5]` → check `inorder_traversal` yields `[1, 3, 5, 7, 11]`.

#### 🧩 Base Code

```python
class BinarySearchTree(BinarySearchTree):
    def build_from_list(self, values):
        """📦 Build BST from a list of integer values."""
        # Your solution here 🛠️
        pass

# Reuse inorder_traversal from Challenge 4 for test 5:
def inorder_traversal(node, result):
    if node is None:
        return
    inorder_traversal(node.left, result)
    result.append(node.value)
    inorder_traversal(node.right, result)

# 🧪 Test cases
def test_build_from_list():
    # Test 1: Empty list
    bst = BinarySearchTree()
    bst.build_from_list([])
    print("📭 Test 1:", bst.root is None)
    # Test 2: Single element
    bst = BinarySearchTree()
    bst.build_from_list([5])
    print("🌱 Test 2:", bst.root is not None and bst.root.value == 5)
    # Test 3: Multiple insert
    bst = BinarySearchTree()
    bst.build_from_list([10, 5, 15])
    cond3 = (bst.root.left.value == 5 and bst.root.right.value == 15)
    print("🔄 Test 3:", cond3)
    # Test 4: Duplicates
    bst = BinarySearchTree()
    bst.build_from_list([10, 10, 10])
    cond4 = (bst.root.value == 10 and bst.root.right.value == 10 and bst.root.right.right.value == 10)
    print("🔁 Test 4:", cond4)
    # Test 5: Unsorted order & inorder check
    bst = BinarySearchTree()
    bst.build_from_list([7, 3, 11, 1, 5])
    ordered = []
    inorder_traversal(bst.root, ordered)
    print("📈 Test 5:", ordered == [1, 3, 5, 7, 11])

# 🚀 Run tests
test_build_from_list()
```

#### 💡 Tips

* Simply loop over `values` and call `insert()`.
* Reuse your previously implemented `insert` method—do not reimplement insertion logic here.

#### 🧠 Motivation

Bulk-building from a list is practical when initializing a BST from a dataset (e.g., reading keys from a file).

---

### 🧩 Inorder Traversal of BST

#### ❓ Problem

Implement the function `inorder_traversal(node, result_list)` to produce a sorted list of BST values.

#### 📜 Description

* Given `node` (root of a BST) and an empty list `result_list`, perform an **in-order traversal**:

  1. If `node is None`, return immediately.
  2. Recurse on `node.left`, appending values to `result_list`.
  3. Append `node.value` to `result_list`.
  4. Recurse on `node.right`.
* After the call, `result_list` must contain the BST keys in **ascending order**.

#### 🧪 5 Tests to Pass

1. **Empty tree**: `inorder_traversal(None, [])` → returns `[]`.
2. **Single node**: Tree with one node `5` → returns `[5]`.
3. **Simple tree**: Insert `[10, 5, 15]` → returns `[5, 10, 15]`.
4. **Left-skewed**: Insert `[5, 4, 3]` → returns `[3, 4, 5]`.
5. **Complex**: Insert `[7, 3, 11, 1, 5, 9, 13]` → returns `[1, 3, 5, 7, 9, 11, 13]`.

#### 🧩 Base Code

```python
def inorder_traversal(node, result_list):
    """
    📝 Inorder traversal: left → root → right.
    Appends node values to result_list in sorted order.
    """
    # Your solution here 🛠️
    pass

# 🧪 Test cases
def test_inorder_traversal():
    # Test 1: Empty tree
    result = []
    inorder_traversal(None, result)
    print("📭 Test 1:", result == [])
    # Test 2: Single node
    single = Node(5)
    result = []
    inorder_traversal(single, result)
    print("🌱 Test 2:", result == [5])
    # Test 3: Simple tree [10,5,15]
    bst = BinarySearchTree()
    bst.build_from_list([10, 5, 15])
    result = []
    inorder_traversal(bst.root, result)
    print("✅ Test 3:", result == [5, 10, 15])
    # Test 4: Left-skewed [5,4,3]
    bst = BinarySearchTree()
    bst.build_from_list([5, 4, 3])
    result = []
    inorder_traversal(bst.root, result)
    print("👈 Test 4:", result == [3, 4, 5])
    # Test 5: Complex [7,3,11,1,5,9,13]
    bst = BinarySearchTree()
    bst.build_from_list([7, 3, 11, 1, 5, 9, 13])
    result = []
    inorder_traversal(bst.root, result)
    print("📈 Test 5:", result == [1, 3, 5, 7, 9, 11, 13])

# 🚀 Run tests
test_inorder_traversal()
```

#### 💡 Tips

* Use recursion:

  ```python
  if node is None: 
      return
  inorder_traversal(node.left, result_list)
  result_list.append(node.value)
  inorder_traversal(node.right, result_list)
  ```
* Ensure you append **after** left subtree and **before** right subtree.

#### 🧠 Motivation

In-order traversal of a BST yields a **sorted** sequence—crucial for tasks like printing keys in order or validating a BST.

---

### 🧩 Find Minimum Value in BST

#### ❓ Problem

Implement `find_min(self)` in class `BinarySearchTree` that returns the **minimum** integer value stored in the BST, or `None` if the tree is empty.

#### 📜 Description

* In a BST, the leftmost node holds the minimum value.
* Starting at `self.root`, traverse left pointers until you reach a node with `left is None`.
* If `self.root` is `None`, return `None`.
* Otherwise, return the `value` of the leftmost node.

#### 🧪 5 Tests to Pass

1. **Empty tree**: `bst = BinarySearchTree(); bst.find_min()` returns `None`.
2. **Single node**: Insert `5`, then `bst.find_min() == 5`.
3. **Right-skewed**: Insert `[5, 10, 15]`, then `bst.find_min() == 5`.
4. **Left-skewed**: Insert `[5, 4, 3]`, then `bst.find_min() == 3`.
5. **Mixed**: Insert `[10, 5, 15, 2, 7]` → `bst.find_min() == 2`.

#### 🧩 Base Code

```python
class BinarySearchTree(BinarySearchTree):
    def find_min(self):
        """🔎 Return the minimum value in the BST, or None if empty."""
        # Your solution here 🛠️
        pass

# 🧪 Test cases
def test_find_min():
    # Test 1: Empty tree
    bst = BinarySearchTree()
    print("📭 Test 1:", bst.find_min() is None)
    # Test 2: Single node
    bst = BinarySearchTree()
    bst.insert(5)
    print("🌱 Test 2:", bst.find_min() == 5)
    # Test 3: Right-skewed [5,10,15]
    bst = BinarySearchTree()
    for v in [5, 10, 15]:
        bst.insert(v)
    print("👉 Test 3:", bst.find_min() == 5)
    # Test 4: Left-skewed [5,4,3]
    bst = BinarySearchTree()
    for v in [5, 4, 3]:
        bst.insert(v)
    print("👈 Test 4:", bst.find_min() == 3)
    # Test 5: Mixed [10,5,15,2,7]
    bst = BinarySearchTree()
    for v in [10, 5, 15, 2, 7]:
        bst.insert(v)
    print("🔍 Test 5:", bst.find_min() == 2)

# 🚀 Run tests
test_find_min()
```

#### 💡 Tips

* If `self.root is None`, return `None`.
* Otherwise, loop:

  ```python
  current = self.root
  while current.left:
      current = current.left
  return current.value
  ```

#### 🧠 Motivation

Finding the minimum is often the first step in deletion algorithms and in-range queries. It highlights BST’s structure advantage.

---

## o4 Advanced Binary Trees (AVL Insert/Delete, Rotations) 🧩🔁

In this section, you will implement core AVL tree operations: node structure, height calculation, balance factor, rotations, insertion with rebalancing, and deletion with rebalancing.

---

Below are the **five** implementation challenges for **Advanced Binary Trees (AVL)**, with **all methods defined inside their respective classes** (`AVLNode` and `AVLTree`). Each challenge follows the same template as before—just now the functions live within classes.

---

### 🧩 Define AVL Node Structure

#### ❓ Problem

Create a class `AVLNode` that stores an integer key, left/right children, and a `height` attribute initialized to 1.

#### 📜 Description

* Implement `__init__(self, key)` so that:

  1. `self.key = key`
  2. `self.left = None`
  3. `self.right = None`
  4. `self.height = 1`

#### 🧪 5 Tests to Pass

1. Creating `node = AVLNode(10)` → `node.key == 10`
2. `node.left` is `None`.
3. `node.right` is `None`.
4. `node.height == 1`.
5. Creating `n2 = AVLNode(-5)` → `n2.key == -5` and `n2.height == 1`.

#### 🧩 Base Code

```python
class AVLNode:
    def __init__(self, key):
        """🌱 Initialize an AVL node with key and default height=1."""
        # Your solution here 🛠️
        pass

# 🧪 Test cases
def test_avl_node():
    n = AVLNode(10)
    print("🔑 Test 1:", n.key == 10)
    print("📐 Test 2:", n.left is None)
    print("📐 Test 3:", n.right is None)
    print("📏 Test 4:", n.height == 1)
    n2 = AVLNode(-5)
    print("🔑 Test 5:", n2.key == -5 and n2.height == 1)

# 🚀 Run tests
test_avl_node()
```

#### 💡 Tips

* Simply assign each attribute in `__init__`.
* `height` starts at 1 for a new leaf node.

#### 🧠 Motivation

Every AVL node must track its subtree height to detect imbalances. A correct node structure is the foundation of rotations.

---

### 🧩 Height Utility & Balance Factor

#### ❓ Problem

Inside an `AVLTree` class, implement two methods:

1. `get_height(self, node)` – returns the `height` of an `AVLNode` or `0` if `node is None`.
2. `get_balance(self, node)` – returns `get_height(node.left) - get_height(node.right)`, or `0` if `node is None`.

#### 📜 Description

* Both methods belong to `class AVLTree`.
* Do not modify their signatures.
* If `node is None`, `get_height` returns `0`, and `get_balance` returns `0`.
* Otherwise, return the appropriate integer.

#### 🧪 5 Tests to Pass

1. `get_height(None) == 0`
2. For `n = AVLNode(5)`, `get_height(n) == 1`.
3. After setting `n.left = AVLNode(3); n.left.height = 2`, `get_height(n.left) == 2`.
4. For empty node, `get_balance(None) == 0`.
5. If

   ```python
   n.left.height = 2
   n.right = AVLNode(8); n.right.height = 1
   ```

   then `get_balance(n) == 2 - 1 == 1`.

#### 🧩 Base Code

```python
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """🔄 AVL Tree with height and balance utilities."""
    def get_height(self, node):
        """
        📏 Return height of AVL node or 0 if node is None.
        """
        # Your solution here 🛠️
        pass

    def get_balance(self, node):
        """
        ⚖️ Return balance factor: height(left) - height(right), or 0 if node is None.
        """
        # Your solution here 🛠️
        pass

# 🧪 Test cases
def test_height_and_balance():
    tree = AVLTree()
    print("📭 Test 1:", tree.get_height(None) == 0)
    n = AVLNode(5)
    print("🌱 Test 2:", tree.get_height(n) == 1)
    n.left = AVLNode(3)
    n.left.height = 2
    print("👈 Test 3:", tree.get_height(n.left) == 2)
    print("📭 Test 4:", tree.get_balance(None) == 0)
    n.right = AVLNode(8)
    n.right.height = 1
    print("📏 Test 5:", tree.get_balance(n) == 1)

# 🚀 Run tests
test_height_and_balance()
```

#### 💡 Tips

* Check for `None` first in each method.
* For `get_balance`, simply call `get_height(node.left)` and `get_height(node.right)`.

#### 🧠 Motivation

Accurate height & balance factor detection is crucial to decide when rotations are needed for O(log n) guarantees.

---

### 🧩 Perform Rotations (Left & Right)

#### ❓ Problem

Inside `AVLTree`, implement two methods:

* `left_rotate(self, z)` – performs a left rotation on node `z` (RR case), returns the new root.
* `right_rotate(self, z)` – performs a right rotation on node `z` (LL case), returns the new root.

#### 📜 Description

* Both methods belong to `class AVLTree`.
* You may call the previous `get_height(...)` method to update heights.
* **Left Rotate** steps (RR case):

  1. Let `y = z.right` and `T2 = y.left`.
  2. Perform rotation:

     ```python
     y.left = z
     z.right = T2
     ```
  3. Update heights:

     ```python
     z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
     y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
     ```
  4. Return `y`.
* **Right Rotate** (LL case) is symmetric.

#### 🧪 5 Tests to Pass

1. **Left Rotate Simple**

   ```python
   tree = AVLTree()
   z = AVLNode(10)
   z.right = AVLNode(20); z.right.height = 1
   z.height = 2
   new_root = tree.left_rotate(z)
   # new_root.key == 20, new_root.left.key == 10, new_root.left.right is None
   print(... )
   ```
2. **Right Rotate Simple**

   ```python
   tree = AVLTree()
   z = AVLNode(20)
   z.left = AVLNode(10); z.left.height = 1
   z.height = 2
   new_root = tree.right_rotate(z)
   # new_root.key == 10, new_root.right.key == 20, new_root.right.left is None
   print(... )
   ```
3. **Update Heights Left**

   ```python
   tree = AVLTree()
   z = AVLNode(30)
   z.right = AVLNode(40); z.right.height = 1
   z.height = 2
   new_root = tree.left_rotate(z)
   # new_root.height == 2 and new_root.left.height == 1
   print(... )
   ```
4. **Update Heights Right**

   ```python
   tree = AVLTree()
   z = AVLNode(30)
   z.left = AVLNode(20); z.left.height = 1
   z.height = 2
   new_root = tree.right_rotate(z)
   # new_root.height == 2 and new_root.right.height == 1
   print(... )
   ```
5. **Chain Left Rotate**

   ```python
   tree = AVLTree()
   root = AVLNode(20)
   root.right = AVLNode(30); root.right.height = 2
   root.right.right = AVLNode(40); root.right.right.height = 1
   root.height = 3
   new_root = tree.left_rotate(root)
   # new_root.key == 30, new_root.left.key == 20, new_root.right.key == 40
   print(... )
   ```

#### 🧩 Base Code

```python
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """🔄 AVL Tree with rotation methods."""
    def get_height(self, node):
        return 0 if not node else node.height

    def get_balance(self, node):
        return 0 if not node else self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        """
        🔄 Perform left rotation on node z and return new root.
        """
        # Your solution here 🛠️
        pass

    def right_rotate(self, z):
        """
        🔃 Perform right rotation on node z and return new root.
        """
        # Your solution here 🛠️
        pass

# 🧪 Test cases
def test_rotations():
    tree = AVLTree()
    # Test 1: Left Rotate Simple
    z = AVLNode(10)
    z.right = AVLNode(20)
    z.right.height = 1
    z.height = 2
    new_root = tree.left_rotate(z)
    cond1 = (new_root.key == 20 and new_root.left.key == 10 and new_root.left.right is None)
    print("🔄 Test 1:", cond1)

    # Test 2: Right Rotate Simple
    z = AVLNode(20)
    z.left = AVLNode(10)
    z.left.height = 1
    z.height = 2
    new_root = tree.right_rotate(z)
    cond2 = (new_root.key == 10 and new_root.right.key == 20 and new_root.right.left is None)
    print("🔃 Test 2:", cond2)

    # Test 3: Update Heights Left
    z = AVLNode(30)
    z.right = AVLNode(40); z.right.height = 1
    z.height = 2
    new_root = tree.left_rotate(z)
    cond3 = (new_root.height == 2 and new_root.left.height == 1)
    print("📏 Test 3:", cond3)

    # Test 4: Update Heights Right
    z = AVLNode(30)
    z.left = AVLNode(20); z.left.height = 1
    z.height = 2
    new_root = tree.right_rotate(z)
    cond4 = (new_root.height == 2 and new_root.right.height == 1)
    print("📐 Test 4:", cond4)

    # Test 5: Chain Left Rotate
    root = AVLNode(20)
    root.right = AVLNode(30); root.right.height = 2
    root.right.right = AVLNode(40); root.right.right.height = 1
    root.height = 3
    new_root = tree.left_rotate(root)
    cond5 = (new_root.key == 30 and new_root.left.key == 20 and new_root.right.key == 40)
    print("🔁 Test 5:", cond5)

# 🚀 Run tests
test_rotations()
```

#### 💡 Tips

* For **left\_rotate**:

  1. `y = z.right`
  2. `T2 = y.left`
  3. Rotate pointers, then update heights.
  4. Return `y`.
* Right rotate is symmetric.

#### 🧠 Motivation

Rotations correct imbalances in O(1) time, ensuring that inserts and deletes remain O(log n).

---

### 🧩 Insert with Rebalancing

#### ❓ Problem

Inside `AVLTree`, implement a method `insert(self, node, key)` that:

1. Performs a normal BST insertion under subtree `node`.
2. Updates `node.height`.
3. Computes `balance = self.get_balance(node)`.
4. Applies one of the four rotation cases (LL, RR, LR, RL) if `balance` goes out of `[-1,1]`.
5. Returns the (possibly new) subtree root.

#### 📜 Description

* Signature: `def insert(self, node, key) -> AVLNode`.
* If `node is None`, return `AVLNode(key)`.
* Recurse: if `key < node.key`, `node.left = insert(node.left, key)` else `node.right = insert(node.right, key)`.
* After recursion, update:

  ```python
  node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
  balance = self.get_balance(node)
  ```
* **LL**: `if balance > 1 and key < node.left.key: return self.right_rotate(node)`
* **RR**: `if balance < -1 and key > node.right.key: return self.left_rotate(node)`
* **LR**: `if balance > 1 and key > node.left.key: node.left = self.left_rotate(node.left); return self.right_rotate(node)`
* **RL**: `if balance < -1 and key < node.right.key: node.right = self.right_rotate(node.right); return self.left_rotate(node)`
* Otherwise `return node`.

#### 🧪 5 Tests to Pass

1. **Simple Insert**:

   ```python
   tree = AVLTree()
   root = tree.insert(None, 10)
   print("🌱 Test 1:", root.key == 10 and root.height == 1)
   ```
2. **LL Case**:

   ```python
   tree = AVLTree()
   root = None
   for k in [30, 20, 10]:
       root = tree.insert(root, k)
   # After LL rebalance, root.key == 20, left.key == 10, right.key == 30
   print("➙ Test 2:", root.key == 20 and root.left.key == 10 and root.right.key == 30)
   ```
3. **RR Case**:

   ```python
   tree = AVLTree()
   root = None
   for k in [10, 20, 30]:
       root = tree.insert(root, k)
   print("➙ Test 3:", root.key == 20 and root.left.key == 10 and root.right.key == 30)
   ```
4. **LR Case**:

   ```python
   tree = AVLTree()
   root = None
   for k in [30, 10, 20]:
       root = tree.insert(root, k)
   print("🔄 Test 4:", root.key == 20 and root.left.key == 10 and root.right.key == 30)
   ```
5. **RL Case**:

   ```python
   tree = AVLTree()
   root = None
   for k in [10, 30, 20]:
       root = tree.insert(root, k)
   print("🔁 Test 5:", root.key == 20 and root.left.key == 10 and root.right.key == 30)
   ```

#### 🧩 Base Code

```python
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """⚙️ AVL Tree with insert/rebalance."""
    def get_height(self, node):
        return 0 if not node else node.height

    def get_balance(self, node):
        return 0 if not node else self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        """🔄 Left rotate (RR case)."""
        # Assume implemented from Challenge 3
        pass

    def right_rotate(self, z):
        """🔃 Right rotate (LL case)."""
        # Assume implemented from Challenge 3
        pass

    def insert(self, node, key):
        """
        ➕ Insert key into AVL subtree rooted at node, rebalance if needed, return new root.
        """
        # Your solution here 🛠️
        pass

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
```

#### 💡 Tips

* Follow this order exactly:

  1. **BST insert**
  2. **Update height**
  3. **Compute balance**
  4. **Rotate if needed**
* Compare `key` vs. `node.left.key` or `node.right.key` to identify LL/LR/RR/RL.

#### 🧠 Motivation

Balanced insertion keeps the tree height within O(log n), guaranteeing efficient lookups.

---

### 🧩 Delete with Rebalancing

#### ❓ Problem

Inside `AVLTree`, implement a method `delete(self, node, key)` that:

1. Performs a standard BST deletion of `key` under subtree `node`.
2. If the node has two children, replaces its key with the in-order successor’s key (`min_value_node(node.right)`).
3. Updates `node.height`.
4. Computes `balance = self.get_balance(node)`.
5. Rebalances via the four rotation cases if `balance` goes out of `[-1,1]`.
6. Returns the (possibly new) subtree root after deletion.

#### 📜 Description

* Signature: `def delete(self, node, key) -> AVLNode`.
* If `node is None`, return `None`.
* Recurse: if `key < node.key`, `node.left = delete(node.left, key)`; elif `key > node.key`, `node.right = delete(node.right, key)`.
* When `key == node.key`:

  1. **No child**: return `None`.
  2. **One child**: return whichever child isn’t `None`.
  3. **Two children**:

     ```python
     temp = self.min_value_node(node.right)
     node.key = temp.key
     node.right = delete(node.right, temp.key)
     ```
* After deletion steps, update:

  ```python
  node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
  balance = self.get_balance(node)
  ```
* **Left-heavy** (`balance > 1`):

  * If `self.get_balance(node.left) >= 0`: **LL** → `return self.right_rotate(node)`
  * Else **LR**:

    ```python
    node.left = self.left_rotate(node.left)
    return self.right_rotate(node)
    ```
* **Right-heavy** (`balance < -1`):

  * If `self.get_balance(node.right) <= 0`: **RR** → `return self.left_rotate(node)`
  * Else **RL**:

    ```python
    node.right = self.right_rotate(node.right)
    return self.left_rotate(node)
    ```
* Otherwise `return node`.

#### 🧪 5 Tests to Pass

1. **Delete Leaf**:

   ```python
   tree = AVLTree()
   root = None
   for k in [20, 10, 30]:
       root = tree.insert(root, k)
   root = tree.delete(root, 10)
   result = []
   def inorder(n, r): 
       if n: 
           inorder(n.left, r); r.append(n.key); inorder(n.right, r)
   inorder(root, result)
   print("🍂 Test 1:", result == [20, 30])
   ```
2. **Delete Node with One Child**:

   ```python
   tree = AVLTree()
   root = None
   for k in [20, 10, 30, 5]:
       root = tree.insert(root, k)
   root = tree.delete(root, 10)
   result = []
   inorder(root, result)
   print("🔄 Test 2:", result == [5, 20, 30])
   ```
3. **Delete Node with Two Children**:

   ```python
   tree = AVLTree()
   root = None
   for k in [20, 10, 30, 5, 15]:
       root = tree.insert(root, k)
   root = tree.delete(root, 10)
   result = []
   inorder(root, result)
   print("✅ Test 3:", result == [5, 15, 20, 30])
   ```
4. **Rebalance After Deletion (LL)**:

   ```python
   tree = AVLTree()
   root = None
   for k in [30, 20, 10, 5]:
       root = tree.insert(root, k)
   root = tree.delete(root, 5)
   result = []
   inorder(root, result)
   print("👈 Test 4:", result == [10, 20, 30])
   ```
5. **Rebalance After Deletion (RR)**:

   ```python
   tree = AVLTree()
   root = None
   for k in [10, 20, 30, 40]:
       root = tree.insert(root, k)
   root = tree.delete(root, 10)
   result = []
   inorder(root, result)
   print("👉 Test 5:", result == [20, 30, 40])
   ```

#### 🧩 Base Code

```python
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """🔄 AVL Tree with delete/rebalance."""
    def get_height(self, node):
        return 0 if not node else node.height

    def get_balance(self, node):
        return 0 if not node else self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        """🔄 Left rotation (RR case)."""
        # Assume implemented from Challenge 3
        pass

    def right_rotate(self, z):
        """🔃 Right rotation (LL case)."""
        # Assume implemented from Challenge 3
        pass

    def min_value_node(self, node):
        """📏 Return node with smallest key in subtree rooted at node."""
        current = node
        while current.left:
            current = current.left
        return current

    def insert(self, node, key):
        """
        ➕ Insert key into AVL subtree rooted at node, rebalance if needed.
        (Implemented in previous challenge.)
        """
        # Assume implemented correctly
        pass

    def delete(self, node, key):
        """
        ➖ Delete key from AVL subtree rooted at node, rebalance if needed.
        """
        # Your solution here 🛠️
        pass

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
```

#### 💡 Tips

* Reuse `min_value_node(...)`, rotation methods, and `get_height(...)`.
* Update `height` before computing `balance`.
* Perform exactly the same rotation cases as in `insert`.

#### 🧠 Motivation

Deletion plus rebalancing preserves AVL’s O(log n) performance, even when removing nodes.

---

💡 *Created with AI support by Elliot Garamendi 👨‍💻*
🤖 *Assisted by ChatGPT – Your creative teaching co-pilot 🚀*
