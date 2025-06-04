# ✨ Midterm Exam: Trees & Advanced Trees Implementation 🌳🚀

This exam assesses your ability to implement core functionalities of **Generic Trees** and **Expression Trees** (Topic 9) in Python. You have **50 minutes** to solve all problems. Each implementation challenge includes automated test cases—each `print(True)` is worth **1 point**. Use only the provided method signatures, and adhere to best practices with descriptive variable names, clear comments, and ample emojis for engagement! 🎯🐍

---

## o1 🛠️ Generic & Expression Trees 🌲 by @elliotgaramendi 👨‍💻

In this section, you will implement core operations for **Generic Trees** and **Expression Trees**. The **Common Code** below defines essential constructors; each challenge focuses on a single method so you don’t need to reimplement unrelated functionality. Use the common classes to build and manipulate trees, then implement only the specified method.

---

### Common Code (Shared by All Challenges in o1)

```python
class GenericTreeNode:
    """🌳 Node for a generic tree (multiple children)."""
    def __init__(self, value):
        self.value = value      # 📊 Data stored in node
        self.children = []      # 👶 List of child nodes

class GenericTree:
    """🌿 Generic tree with basic operations."""
    def __init__(self):
        self.root = None        # 🌱 Root of the generic tree

class ExprNode:
    """🔢 Node for an expression tree (operator or operand)."""
    def __init__(self, value):
        self.value = value      # Operator (str) or operand (str/number)
        self.left = None        # ↙️ Left child
        self.right = None       # ↘️ Right child
    
    def is_operator(self):
        return self.value in ['+', '-', '*', '/']

class ExpressionTree:
    """📝 Binary tree for building and traversing expressions."""
    def __init__(self):
        self.root = None        # 🌱 Root of expression tree

class EvaluableExpressionTree(ExpressionTree):
    """🧮 Extension of ExpressionTree that can be evaluated."""
    def __init__(self):
        super().__init__()
```

---

### 🧩 Challenge 1: Generic Tree Node Insertion

#### ❓ Problem

Implement the method `add_child(self, value)` in the `GenericTreeNode` class to insert a new child node under the given parent node.

#### 📜 Description

* You have a `GenericTreeNode` where each node holds a `value` and a list of `children`.
* Complete the `add_child(self, value)` method so that it:

  1. Creates a new `GenericTreeNode` with the given `value`.
  2. Appends it to `self.children`.
  3. Returns the newly created child node.
* **Do not** modify the constructor or any other part of the class.

#### 🧪 5 Tests to Pass

1. Insert one child under a root; verify `root.children[0].value` matches.
2. Insert two children under the same parent; verify order and values (`["B", "C"]`).
3. Insert a child under a child node; verify grandchild relationship.
4. Call `add_child()` on a leaf; verify its `children` list is no longer empty.
5. Ensure multiple siblings maintain correct order (no duplicates).

#### 🧩 Base Code

```python
class GenericTreeNode:
    """Node for generic tree with multiple children."""
    def __init__(self, value):
        self.value = value      # 📊 Data stored in node
        self.children = []      # 👶 List of child nodes
    
    def add_child(self, value):
        """➕ Add a child node with the given value, return the new node."""
        # Your solution here 🛠️
        pass

# 🧪 Test cases
def test_add_child():
    root = GenericTreeNode("A")
    # Test 1
    child1 = root.add_child("B")
    print("🌳 Test 1:", root.children[0].value == "B")
    # Test 2
    child2 = root.add_child("C")
    print("🌳 Test 2:", [c.value for c in root.children] == ["B", "C"])
    # Test 3
    grandchild = child1.add_child("D")
    print("🌳 Test 3:", child1.children[0].value == "D")
    # Test 4
    leaf = GenericTreeNode("X")
    new_grand = leaf.add_child("Y")
    print("🌳 Test 4:", leaf.children[0].value == "Y")
    # Test 5
    root.add_child("E")
    print("🌳 Test 5:", [c.value for c in root.children] == ["B", "C", "E"])

# 🚀 Run tests
test_add_child()
```

#### 💡 Tips

* Use `self.children.append(new_node)` to preserve sibling order.
* Always **return** the newly created node for chaining.
* Keep variable names clear (`new_node`, `child_node`, etc.) for readability. 🔍

#### 🧠 Motivation

Generic trees model hierarchical data (e.g., file systems, organizational charts). Mastering node insertion is the first step toward advanced traversals and manipulations. 🌐📂

---

### 🧩 Challenge 2: Generic Tree Preorder Traversal

#### ❓ Problem

Implement the method `preorder_traversal(self, node=None, result=None)` in the `GenericTree` class to return a list of node values in **preorder** (visit node, then children left-to-right).

#### 📜 Description

* Given a `GenericTree` instance (with `self.root` as a `GenericTreeNode` or `None`), implement `preorder_traversal(self, node=None, result=None)` such that:

  1. If `node` is `None`, default to `self.root`.
  2. If `result` is `None`, default to an empty list `[]`.
  3. If `node` is `None` (empty tree), return `result` (which is `[]`).
  4. Append `node.value` to `result`.
  5. For each `child` in `node.children` (left-to-right), recurse `preorder_traversal(child, result)`.
  6. Return `result` after traversal completes.
* **Do not** modify the constructor or node definitions.

#### 🧪 5 Tests to Pass

1. **Empty tree**: `tree = GenericTree()` → `tree.preorder_traversal()` returns `[]`.
2. **Single-node tree**: Root with value `42` → returns `[42]`.
3. **Two-level tree**: Root `A` with children `B`, `C` → returns `["A", "B", "C"]`.
4. **Three-level, varying children** (see layout below) → correct nested preorder.
5. **No duplicates**: Verify returned list length equals unique count.

*Example structure for Test 3 and Test 4:*

```
      A
    / | \
   B  C  D
      |
      E
```

#### 🧩 Base Code

```python
class GenericTreeNode:
    """🌳 Node for a generic tree (multiple children)."""
    def __init__(self, value):
        self.value = value
        self.children = []

class GenericTree:
    """🌿 Generic tree with basic operations."""
    def __init__(self):
        self.root = None  # 🌱 Root of the generic tree

    def preorder_traversal(self, node=None, result=None):
        """
        📝 Visit node first, then all children (DLR) in left-to-right order.
        Returns a list of values in preorder.
        """
        # Your solution here 🛠️
        pass

# 🧪 Test cases
def test_generic_preorder():
    # Test 1: Empty tree
    tree = GenericTree()
    print("🚶 Test 1:", tree.preorder_traversal() == [])

    # Build tree:
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

    # Test 2: Two-level
    print("🚶 Test 2:", tree.preorder_traversal() == ["A", "B", "C", "E", "D"])

    # Test 3: Single-node after resetting
    single = GenericTree()
    single.root = GenericTreeNode(42)
    print("🚶 Test 3:", single.preorder_traversal() == [42])

    # Test 4: More complex (add extra children)
    c.add_child("F")
    b.add_child("G")
    print("🚶 Test 4:", tree.preorder_traversal() == ["A", "B", "G", "C", "E", "F", "D"])

    # Test 5: Verify no duplication
    values = tree.preorder_traversal()
    print("🚶 Test 5:", len(values) == len(set(values)))

# 🚀 Run tests
test_generic_preorder()
```

#### 💡 Tips

* Initialize `result` only once at the start:

  ```python
  if result is None:
      result = []
  ```
* If `node is None`, simply return `result`.
* Append current node’s value, then loop over `node.children` and recurse.

#### 🧠 Motivation

Preorder traversal is essential for tasks like **serializing** hierarchical data (e.g., saving a folder structure). It also underpins many tree-based algorithms such as expression evaluation and tree-copying. 🌿🔄

---

### 🧩 Challenge 3: Expression Tree Build from Prefix

#### ❓ Problem

Implement the method `build_from_prefix(self, prefix_tokens)` in the `ExpressionTree` class to construct a binary expression tree from a list of **prefix** (Polish) tokens.

#### 📜 Description

* The `ExpressionTree` class has `self.root = None`.
* `prefix_tokens` is a list of strings (e.g., `["*", "+", "2", "3", "4"]`).
* Operators: `{"+", "-", "*", "/"}`; operands: numeric strings (e.g., `"2"`) or variable names (e.g., `"x"`).
* **Algorithm** (standard stack approach):

  1. Process `prefix_tokens` in **reverse order**.
  2. For each token:

     * If it’s an operand, create `ExprNode(token)` and **push** onto `stack`.
     * If it’s an operator, **pop** two nodes (`left_node = stack.pop()`, then `right_node = stack.pop()`), create `ExprNode(token)` as `node`, set `node.left = left_node` and `node.right = right_node`, then **push** `node` back.
  3. After all tokens, **pop** the last node from `stack` and assign to `self.root`.
  4. If `prefix_tokens` is empty, leave `self.root = None`.
* **Do not** modify constructors or other methods.

#### 🧪 5 Tests to Pass

1. Prefix `["+", "2", "3"]` → `root.value == "+"`, `root.left.value == "2"`, `root.right.value == "3"`.
2. Prefix `["*", "+", "1", "2", "3"]` → `(1+2)*3`:

   * `root.value == "*"`,
   * `root.left.value == "+"`,
   * `root.left.left.value == "1"`,
   * `root.left.right.value == "2"`,
   * `root.right.value == "3"`.
3. Prefix with variables: `["-", "x", "y"]` → `root.value == "-"`, children `"x"`, `"y"`.
4. Longer prefix: `["-", "*", "2", "3", "/", "8", "4"]` → `((2*3) - (8/4))`.
5. Empty or invalid list: `prefix_tokens = []` → `self.root` remains `None`.

#### 🧩 Base Code

```python
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
        # Your solution here 🛠️
        pass

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
```

#### 💡 Tips

* Use a Python **list as a stack**: `stack.append(node)` to push, `stack.pop()` to pop.
* Always **reverse** `prefix_tokens` so you process from the end to the front.
* For each operator, **pop two** nodes (first pop is left child, second pop is right child). 🔄

#### 🧠 Motivation

Building from prefix equips you to parse expressions in compilers and calculators. Understanding prefix vs. postfix strengthens your grasp of parsing algorithms. 🧮🔣

---

### 🧩 Challenge 4: Expression Tree Inorder Conversion

#### ❓ Problem

Implement `infix_traversal(self, node=None)` in the `ExpressionTree` class to produce the **infix** (human-readable) notation string from the tree, adding parentheses to reflect proper precedence.

#### 📜 Description

* Given an `ExpressionTree` instance, implement `infix_traversal(self, node=None)` such that:

  1. If `node` is `None`, start at `self.root`.
  2. If `node` itself is `None`, return `""` (empty string).
  3. If `not node.is_operator()`, return `node.value` (operand as string).
  4. Otherwise (operator), recursively:

     * `left_str = infix_traversal(node.left)`
     * `right_str = infix_traversal(node.right)`
     * Return `f"({left_str} {node.value} {right_str})"`.
* **Do not** modify constructors or other methods.

#### 🧪 5 Tests to Pass

1. **Empty tree**: `tree.infix_traversal()` returns `""`.
2. **Single operand**: Tree with root `ExprNode("42")` → returns `"42"`.
3. **Simple binary**: Prefix `["+", "2", "3"]` → returns `"(2 + 3)"`.
4. **Nested**: Prefix `["*", "+", "2", "3", "4"]` → `((2 + 3) * 4)`.
5. **More complex**: Prefix `["-", "*", "1", "2", "/", "8", "4"]` → `"((1 * 2) - (8 / 4))"`.

#### 🧩 Base Code

```python
class ExprNode:
    """🔢 Node for an expression tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def is_operator(self):
        return self.value in ['+', '-', '*', '/']

class ExpressionTree:
    """📝 Binary tree for building and traversing expressions."""
    def __init__(self):
        self.root = None  # 🌱 Root of the expression tree

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
    print("📝 Test 1:", tree.infix_traversal() == "")
    # Build (2 + 3)
    root = ExprNode("+")
    root.left = ExprNode("2")
    root.right = ExprNode("3")
    tree.root = root
    print("📝 Test 2:", tree.infix_traversal() == "(2 + 3)")
    # Build ((2+3)*4)
    root = ExprNode("*")
    left = ExprNode("+"); left.left = ExprNode("2"); left.right = ExprNode("3")
    root.left = left; root.right = ExprNode("4")
    tree.root = root
    print("📝 Test 3:", tree.infix_traversal() == "((2 + 3) * 4)")
    # Build ((1*2) - (8/4))
    root = ExprNode("-")
    l = ExprNode("*"); l.left = ExprNode("1"); l.right = ExprNode("2")
    r = ExprNode("/"); r.left = ExprNode("8"); r.right = ExprNode("4")
    root.left = l; root.right = r
    tree.root = root
    print("📝 Test 4:", tree.infix_traversal() == "((1 * 2) - (8 / 4))")
    # Test 5: Single operand
    tree.root = ExprNode("X")
    print("📝 Test 5:", tree.infix_traversal() == "X")

# 🚀 Run tests
test_infix_traversal()
```

#### 💡 Tips

* Check early:

  ```python
  if node is None:
      return ""
  ```
* If the node is not an operator (`not node.is_operator()`), return `node.value`.
* Otherwise, build strings for left and right, then wrap with parentheses. 🔄

#### 🧠 Motivation

Infix conversion with parentheses is crucial in compilers and expression evaluators to preserve operator precedence. It’s a fundamental step in many language interpreters and calculators. 📚🔣

---

### 🧩 Challenge 5: Expression Tree Evaluation with Variables

#### ❓ Problem

Implement `evaluate_with_variables(self, variables)` in the `EvaluableExpressionTree` class to compute the numeric result of an expression tree containing both numbers and variable names, given a dictionary mapping variables to numeric values.

#### 📜 Description

* Given an `EvaluableExpressionTree` whose leaves are:

  * **Numeric strings** (e.g., `"5"`)
  * **Variable names** (e.g., `"x"`)
* Implement:

  ```python
  def evaluate_with_variables(self, variables):
      """
      Evaluate the expression tree using the provided dictionary `variables`.
      """
  ```
* **Behavior**:

  * If a leaf’s `value` is in `variables`, use `float(variables[value])`.
  * Otherwise, attempt `float(node.value)`; if it fails, raise `ValueError("Unknown variable: {value}")`.
  * For operators (`+, -, *, /`), recursively evaluate left/right subtrees:

    * Left result = `evaluate_with_variables(node.left, variables)`
    * Right result = `evaluate_with_variables(node.right, variables)`
    * Apply `node.value` operator:

      * Division by zero: `if right_result == 0 → raise ValueError("Division by zero!")`.
      * Return result as `float`.
* **Do not** modify constructors or helper-building methods.

#### 🧪 5 Tests to Pass

1. Tree representing `"2 3 +"` (postfix build) with empty `variables` → returns `5.0`.
2. Tree representing `"x 4 *"` with `{"x": 2}` → returns `8.0`.
3. Tree representing `"x y -"` with `{"x": 5, "y": 3}` → returns `2.0`.
4. Tree `"a b /"` with `{"a": 8, "b": 0}` → raises `ValueError("Division by zero!")`.
5. Tree `"x z +"` with `{"x": 1}` → raises `ValueError("Unknown variable: z")`.

*Use the helper `build_expression_tree(postfix)` provided to set `tree.root`.*

#### 🧩 Base Code

```python
class ExprNode:
    """🔢 Node for expression tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def is_operator(self):
        return self.value in ['+', '-', '*', '/']

class EvaluableExpressionTree(ExpressionTree):
    """🧮 Expression tree that can be evaluated with variables."""
    def __init__(self):
        super().__init__()  # Initializes self.root = None

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
```

#### 💡 Tips

* **Leaf handling**:

  ```python
  if not node.is_operator():
      if node.value in variables:
          return float(variables[node.value])
      try:
          return float(node.value)
      except:
          raise ValueError(f"Unknown variable: {node.value}")
  ```
* **Operator handling**:

  ```python
  left_val = self.evaluate_with_variables(node.left, variables)
  right_val = self.evaluate_with_variables(node.right, variables)
  if node.value == "/" and right_val == 0:
      raise ValueError("Division by zero!")
  # then apply operator
  ```
* Use recursion to evaluate subtrees before applying the operator. 🔄

#### 🧠 Motivation

Evaluating expressions with variables is key in **interpreters**, **symbolic math**, and **data analysis**. This challenge bridges parsing (building tree) and evaluation (computing result), foundational for compiler design and scientific computing. 🧙‍♂️📊

---

💡 *Created with AI support by Elliot Garamendi 👨‍💻*
🤖 *Assisted by ChatGPT – Your creative teaching co-pilot 🚀*

---

## o2 🛠️ Expression Trees (Parsing & Evaluation) 🌲 by @elliotgaramendi 👨‍💻

In this section, you will build, traverse, evaluate, convert, and simplify expression trees. The **Common Code** provides only class definitions—no implementations—so you focus on each challenge’s method. Embrace the emojis and have fun! 🎉🐍

---

### Common Code (Shared by All Challenges in o2)

```python
class Node:
    """🔢 Node for an expression tree (operator or operand)."""
    def __init__(self, value):
        self.value = value        # Operator (str) or operand (str/number)
        self.left = None          # ↙️ Left child
        self.right = None         # ↘️ Right child

    def is_operator(self):
        return self.value in ['+', '-', '*', '/']

class ExpressionTree:
    """🌳 Expression tree with placeholder methods."""
    def __init__(self):
        self.root = None          # 🌱 Root of the expression tree

    # Note: build_from_postfix, inorder, preorder, postorder,
    # evaluate, and simplify are implemented in individual challenges below.
```


---

### 🧩 Challenge 1: Build Expression Tree from Postfix 🛠️

#### ❓ Problem

Implement `build_from_postfix(self, postfix_tokens)` in `ExpressionTree` to convert **postfix** tokens into an expression tree.

#### 📜 Description

* Use a stack:

  1. `stack = []`.
  2. For each `token` in `postfix_tokens`:

     * If **not** an operator (`+,-,*,/`), push `Node(token)`.
     * Else (operator): pop `right`, pop `left`, create `Node(token)`, set children, push.
  3. At end, set `self.root = stack.pop()` (or `None` if empty).

#### 🧪 5 Tests to Pass

1. **Simple addition**:

   ```python
   tree = ExpressionTree()
   tree.build_from_postfix(["2","3","+"])
   # tree.root.value == "+"; left.value == "2"; right.value == "3"
   ```
2. **Precedence**:

   ```python
   tree = ExpressionTree()
   tree.build_from_postfix(["2","3","4","*","+"])
   # root "+", left "2", right "*"
   ```
3. **Nested**:

   ```python
   tree.build_from_postfix(["1","2","+","3","4","-","*"])
   # root "*", left "+", right "-"
   ```
4. **Variables**:

   ```python
   tree.build_from_postfix(["a","b","c","*","+"])
   # root "+", left "a", right "*"
   ```
5. **Single operand**:

   ```python
   tree.build_from_postfix(["x"])
   # root.value == "x"; no children
   ```

#### 🧩 Base Code

```python
class ExpressionTree:
    def __init__(self):
        self.root = None

    def build_from_postfix(self, postfix_tokens):
        """🔨 Build tree from postfix tokens using a stack."""
        # Your solution here 🛠️
        pass

# 🧪 Test cases
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

# 🚀 Run tests
test_build_from_postfix()
```

#### 💡 Tips

* Use a Python list as a stack: `stack = []`.
* Check operator membership via a set: `ops = {"+", "-", "*", "/"}`.
* When you see a non-operator token, create `Node(token)` and push it.
* When you see an operator, always pop **right** first, then **left**, before creating the new operator node.
* After processing all tokens, if `stack` is nonempty, its sole element is the new `root`.

#### 🧠 Motivation

Parsing postfix into a tree is foundational for compilers and calculators—by building the structure once, you avoid repeated string parsing. Understanding the stack-based method gives insight into efficient expression evaluation.

---

### 🧩 Challenge 2: Evaluate Expression Tree 🧮

#### ❓ Problem

Implement `evaluate(self, node=None)` in `EvaluableExpressionTree` to compute the integer result of the tree (only integer operands and `+,-,*,/`).

#### 📜 Description

* Recursively:

  1. If `node is None`, return `0`.
  2. If `node.left is None and node.right is None`, return `int(node.value)`.
  3. Otherwise:

     * `left_val  = self.evaluate(node.left)`
     * `right_val = self.evaluate(node.right)`
     * Then:

       ```python
       if node.value == "+":  return left_val + right_val
       if node.value == "-":  return left_val - right_val
       if node.value == "*":  return left_val * right_val
       if node.value == "/":  return left_val // right_val
       else: raise ValueError(f"Unsupported operator: {node.value}")
       ```

#### 🧪 5 Tests to Pass

1. **Leaf only**:

   ```python
   tree = EvaluableExpressionTree()
   tree.root = Node("5")
   # evaluate() == 5
   ```
2. **Addition**:

   ```python
   tree = EvaluableExpressionTree()
   tree.build_from_postfix(["2","3","+"])
   # evaluate() == 5
   ```
3. **Mixed**:

   ```python
   tree.build_from_postfix(["2","3","+","4","*"])  # (2+3)*4
   # evaluate() == 20
   ```
4. **Division**:

   ```python
   tree.build_from_postfix(["8","4","/"])
   # evaluate() == 2
   ```
5. **Nested**:

   ```python
   tree.build_from_postfix(["10","5","+","2","*","8","4","/","-"])
   # ((10+5)*2)-(8/4) == 28
   ```

#### 🧩 Base Code

```python
class EvaluableExpressionTree(ExpressionTree):
    def __init__(self):
        super().__init__()

    def evaluate(self, node=None):
        """🧮 Evaluate an expression tree containing integers and +,-,*,/."""
        # Your solution here 🛠️
        pass

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
```


#### 💡 Tips

* Always handle the base case: if `node is None`, return `0`.
* Detect a leaf node by checking `if not node.is_operator()`: it has no children, so simply `return int(node.value)`.
* Recursively compute left and right subexpressions before applying the operator.
* Use integer division (`//`) for the `/` operator to match expected behaviors.
* Raise a clear `ValueError` if you encounter any unexpected operator symbol.

#### 🧠 Motivation

Evaluating a pre-built tree bypasses repeated string parsing and enables fast, recursive computation with clear substructure. This underpins many interpreters, JIT compilers, and query engines.

---

### 🧩 Challenge 3: Traversal Methods 🔄

#### ❓ Problem

Implement `inorder(self, node=None, result=None)`, `preorder(self, node=None, result=None)`, and `postorder(self, node=None, result=None)` in `ExpressionTree` to produce **infix**, **prefix**, and **postfix** token lists, respectively.

#### 📜 Description

* **Inorder** (`left, root, right` with parentheses):

  1. If `node is None`, set `node = self.root`. If still empty, return `result` (initialized to `[]`).
  2. If `node.is_operator()`, `result.append("(")`.
  3. Recurse `inorder(node.left, result)`.
  4. `result.append(node.value)`.
  5. Recurse `inorder(node.right, result)`.
  6. If `node.is_operator()`, `result.append(")")`.
  7. Return `result`.

* **Preorder** (`root, left, right`):

  1. If `node is None`, set `node = self.root`. If still empty, return `result`.
  2. `result.append(node.value)`.
  3. Recurse `preorder(node.left, result)`.
  4. Recurse `preorder(node.right, result)`.
  5. Return `result`.

* **Postorder** (`left, right, root`):

  1. If `node is None`, set `node = self.root`. If still empty, return `result`.
  2. Recurse `postorder(node.left, result)`.
  3. Recurse `postorder(node.right, result)`.
  4. `result.append(node.value)`.
  5. Return `result`.

#### 🧪 5 Tests to Pass

1. For `tree.build_from_postfix(["2","3","+","4","1","-","*"])` → `((2+3)*(4-1))`:

   * **Inorder** → `["(", "(", "2", "+", "3", ")", "*", "(", "4", "-", "1", ")", ")"]`.
   * **Preorder** → `["*", "+", "2", "3", "-", "4", "1"]`.
   * **Postorder** → `["2", "3", "+", "4", "1", "-", "*"]`.
2. **Single node** `"X"`: inorder `["X"]`, preorder `["X"]`, postorder `["X"]`.
3. **Empty tree**: all return `[]`.
4. **Mixed** `(1*(2+3))`:

   * Infix: `["(", "1", "*", "(", "2", "+", "3", ")", ")"]`.
   * Prefix: `["*", "1", "+", "2", "3"]`.
   * Postfix: `["1", "2", "3", "+", "*"]`.
5. **Variables** `(a+(b*c))`:

   * Infix: `["(", "a", "+", "(", "b", "*", "c", ")", ")"]`.
   * Prefix: `["+", "a", "*", "b", "c"]`.
   * Postfix: `["a", "b", "c", "*", "+"]`.

#### 🧩 Base Code

```python
class ExpressionTree:
    """🌳 Expression tree with build and traversal placeholders."""
    def __init__(self):
        self.root = None

    def build_from_postfix(self, postfix_tokens):
        """🔨 Build tree from postfix tokens."""
        stack = []
        ops = {"+", "-", "*", "/"}
        for tok in postfix_tokens:
            node = Node(tok)
            if tok in ops:
                node.right = stack.pop()
                node.left = stack.pop()
            stack.append(node)
        self.root = stack.pop() if stack else None

    def inorder(self, node=None, result=None):
        """📝 Inorder traversal (left, root, right) with parentheses."""
        # Your solution here 🛠️
        pass

    def preorder(self, node=None, result=None):
        """🚀 Preorder traversal (root, left, right) to generate prefix tokens."""
        # Your solution here 🛠️
        pass

    def postorder(self, node=None, result=None):
        """🧠 Postorder traversal (left, right, root) to generate postfix tokens."""
        # Your solution here 🛠️
        pass

# Helper to build for tests
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
    tree = ExpressionTree()
    tree.build_from_postfix(["2","3","+","4","1","-","*"])
    # Inorder
    infix = tree.inorder()
    print("📝 Test 1 (Infix):", "".join(infix) == "((2+3)*(4-1))")
    # Preorder
    prefix = tree.preorder()
    print("🚀 Test 1 (Prefix):", " ".join(prefix) == "* + 2 3 - 4 1")
    # Postorder
    postfix = tree.postorder()
    print("🧠 Test 1 (Postfix):", " ".join(postfix) == "2 3 + 4 1 - *")
    # Single node "X"
    single = ExpressionTree()
    single.root = Node("X")
    print("🌱 Test 2 (Infix):", single.inorder() == ["X"])
    print("🌱 Test 2 (Prefix):", single.preorder() == ["X"])
    print("🌱 Test 2 (Postfix):", single.postorder() == ["X"])
    # Empty tree
    empty = ExpressionTree()
    print("📭 Test 3 (Infix):", empty.inorder() == [])
    print("📭 Test 3 (Prefix):", empty.preorder() == [])
    print("📭 Test 3 (Postfix):", empty.postorder() == [])
    # Mixed operators (1*(2+3))
    tree2 = ExpressionTree()
    tree2.build_from_postfix(["1","2","3","+","*"])
    print("🔄 Test 4 (Infix):", "".join(tree2.inorder()) == "(1*(2+3))")
    print("🔄 Test 4 (Prefix):", " ".join(tree2.preorder()) == "* 1 + 2 3")
    print("🔄 Test 4 (Postfix):", " ".join(tree2.postorder()) == "1 2 3 + *")
    # Variables (a+(b*c))
    tree3 = ExpressionTree()
    tree3.build_from_postfix(["a","b","c","*","+"])
    print("🔤 Test 5 (Infix):", "".join(tree3.inorder()) == "(a+(b*c))")
    print("🔤 Test 5 (Prefix):", " ".join(tree3.preorder()) == "+ a * b c")
    print("🔤 Test 5 (Postfix):", " ".join(tree3.postorder()) == "a b c * +")

# 🚀 Run tests
test_traversals()
```

#### 💡 Tips

* Initialize `result` to an empty list when first called:

  ```python
  if result is None:
      result = []
  ```
* In **inorder**, add `"("` before recursing left if `node.is_operator()`, and add `")"` after recursing right.
* In **preorder**, always append `node.value` first, then recursively visit `node.left` and `node.right`.
* In **postorder**, recursively visit `node.left` and `node.right`, then append `node.value`.
* Guard against an empty tree: if `self.root` is `None`, immediately return `[]`.

#### 🧠 Motivation

Tree traversals map directly to infix, prefix, and postfix notations. Mastering these methods helps you convert between human-readable math and machine-ready representations—crucial for code generation, serialization, and evaluation.

---

### 🧩 Challenge 4: Infix to Postfix Conversion 🔁

#### ❓ Problem

Implement the standalone function `infix_to_postfix(tokens)` to convert **infix** tokens into **postfix** tokens using the shunting-yard algorithm.

#### 📜 Description

* Algorithm:

  1. `output = []`, `stack = []`, `precedence = {"+":1, "-":1, "*":2, "/":2}`.
  2. For each `token` in `tokens`:

     * If `token.isalnum()`: `output.append(token)`.
     * Elif `token == "("`: `stack.append(token)`.
     * Elif `token == ")"`: pop until `"("`, appending to `output`, then pop `"("`.
     * Else (operator): while `stack` top has **≥** precedence, pop to `output`, then `stack.append(token)`.
  3. At end, pop remaining to `output`.
* Return `output`.

#### 🧪 5 Tests to Pass

1. **Simple**:

   ```python
   infix_to_postfix(["2", "+", "3"]) == ["2", "3", "+"]
   ```
2. **Precedence**:

   ```python
   infix_to_postfix(["2", "+", "3", "*", "4"]) ==
   ["2", "3", "4", "*", "+"]
   ```
3. **Parentheses**:

   ```python
   infix_to_postfix(["(", "2", "+", "3", ")", "*", "4"]) ==
   ["2", "3", "+", "4", "*"]
   ```
4. **Complex**:

   ```python
   infix_to_postfix(["(", "1", "+", "2", ")", "*", "(", "3", "-", "4", ")"]) ==
   ["1", "2", "+", "3", "4", "-", "*"]
   ```
5. **Variables**:

   ```python
   infix_to_postfix(["a", "+", "b", "*", "c", "/", "d"]) ==
   ["a", "b", "c", "*", "d", "/", "+"]
   ```

#### 🧩 Base Code

```python
def infix_to_postfix(tokens):
    """
    🔁 Convert a list of infix tokens to postfix notation.
    """
    # Your solution here 🛠️
    pass

# 🧪 Test cases
def test_infix_to_postfix():
    print("➕ Test 1:", infix_to_postfix(["2", "+", "3"]) == ["2", "3", "+"])
    print("📊 Test 2:", infix_to_postfix(["2", "+", "3", "*", "4"]) ==
          ["2", "3", "4", "*", "+"])
    print("🔗 Test 3:", infix_to_postfix(["(", "2", "+", "3", ")", "*", "4"]) ==
          ["2", "3", "+", "4", "*"])
    print("🧮 Test 4:", infix_to_postfix(["(", "1", "+", "2", ")", "*", "(",
                                         "3", "-", "4", ")"]) ==
          ["1", "2", "+", "3", "4", "-", "*"])
    print("🔤 Test 5:", infix_to_postfix(["a", "+", "b", "*", "c", "/", "d"]) ==
          ["a", "b", "c", "*", "d", "/", "+"])

# 🚀 Run tests
test_infix_to_postfix()
```

#### 💡 Tips

* Maintain two lists: `output = []` and `stack = []`.
* Use a precedence dictionary:

  ```python
  prec = {"+": 1, "-": 1, "*": 2, "/": 2}
  ```
* When you see an operand (`token.isalnum()`), append it directly to `output`.
* Push `"("` onto `stack`, and when you see `")"`, pop until encountering `"("` (which you then discard).
* For an operator, pop from `stack` to `output` while the top of `stack` is an operator with **≥** precedence, then push the current operator.
* After processing all tokens, pop any remaining operators from `stack` into `output`.

#### 🧠 Motivation

The shunting-yard algorithm lets you convert infix (human-friendly) expressions into postfix (machine-friendly) in linear time. This underlies most compiler front-ends and calculator engines.


---

### 🧩 Challenge 5: Simplify Expression Tree 🧙‍♂️

#### ❓ Problem

Implement `simplify(self, node=None)` in `EvaluableExpressionTree` to collapse constant-only subtrees into single numeric leaves.

#### 📜 Description

* Recursively:

  1. If `node is None`, return `None`.
  2. `node.left  = self.simplify(node.left)`
     `node.right = self.simplify(node.right)`
  3. If both children are leaves with `value.isdigit()`:

     ```python
     left_val = int(node.left.value)
     right_val = int(node.right.value)
     if node.value == "+":
         res = left_val + right_val
     elif node.value == "-":
         res = left_val - right_val
     elif node.value == "*":
         res = left_val * right_val
     elif node.value == "/":
         res = left_val // right_val
     else:
         return node
     return Node(str(res))
     ```
  4. Else, return `node`.

#### 🧪 5 Tests to Pass

1. **All constants**: `(2 + 3)` → becomes `"5"`.
2. **Mixed**: `(x + 3)` → remains unchanged.
3. **Nested constants**: `((2 * 3) + (8 - 3))` → collapses to `"11"`.
4. **Partial**: `((2 + 3) * (z * 4))` → left → `"5"`, right stays `(z*4)`.
5. **No simplify**: `(x * y)` → remains.

#### 🧩 Base Code

```python
class EvaluableExpressionTree(ExpressionTree):
    def __init__(self):
        super().__init__()

    def simplify(self, node=None):
        """
        🔄 Simplify constant-only subtrees into single numeric leaves.
        """
        # Your solution here 🛠️
        pass

# Helper to build and test (reuse from previous challenge)
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
def test_simplify_expression_tree():
    et = EvaluableExpressionTree()

    # Test 1: All constants (2+3)
    et.root = build_tree(["2", "3", "+"])
    simp = et.simplify()
    print("🔢 Test 1:", simp and simp.value == "5" and simp.left is None and simp.right is None)

    # Test 2: Mixed (x+3)
    et.root = build_tree(["x", "3", "+"])
    simp = et.simplify()
    cond2 = (simp and simp.value == "+" and simp.left.value == "x" and simp.right.value == "3")
    print("🔤 Test 2:", cond2)

    # Test 3: Nested constants ((2*3)+(8-3))
    et.root = build_tree(["2", "3", "*", "8", "3", "-", "+"])
    simp = et.simplify()
    print("🎯 Test 3:", simp and simp.value == "11" and simp.left is None and simp.right is None)

    # Test 4: Partial ((2+3)*(z*4))
    et.root = build_tree(["2", "3", "+", "z", "4", "*", "*"])
    simp = et.simplify()
    cond4 = (simp and simp.value == "*" and simp.left.value == "5" and simp.right.value == "*")
    print("🔄 Test 4:", cond4)

    # Test 5: No simplify (x*y)
    et.root = build_tree(["x", "y", "*"])
    simp = et.simplify()
    print("🌿 Test 5:", simp and simp.value == "*" and simp.left.value == "x" and simp.right.value == "y")

# 🚀 Run tests
test_simplify_expression_tree()
```

#### 💡 Tips

* Start by handling `if node is None: return None` to cover empty trees.
* Recursively simplify left and right subtrees first, updating `node.left` and `node.right`.
* Check if both `node.left` and `node.right` exist and are leaves with `value.isdigit()`.
* Convert both leaf values to `int`, apply the correct operator, then return a new `Node(str(res))`.
* If the operator is not one of `+,-,*,/`, simply return `node` without change.

#### 🧠 Motivation

Collapsing constant-only subtrees optimizes evaluation by reducing tree size. This is a simple form of constant folding used in compilers and symbolic math systems to speed up repeated computations.

---

💡 *Created with AI support by Elliot Garamendi 👨‍💻*
🤖 *Assisted by ChatGPT – Your creative teaching co-pilot 🚀*

---

## o3 Binary Search Trees (BST) & Search 🛠️🌲

In this section, you will implement core BST operations: inserting values, searching for values, building the tree from a list, traversing in-order, and finding the minimum key. Below, the **Common Code** provides only the `Node` class and the `BinarySearchTree` constructor; each challenge includes the necessary dependent methods so you can focus **only** on the required implementation.

---

### Common Code (Shared by All Challenges in o3)

```python
class Node:
    """🌱 Node for Binary Search Tree"""
    def __init__(self, value):
        self.value = value   # 🔢 Node value (int)
        self.left = None     # 🌿 Left child (Node or None)
        self.right = None    # 🌿 Right child (Node or None)

class BinarySearchTree:
    """🌳 Binary Search Tree with core utilities."""
    def __init__(self):
        self.root = None  # 📭 Initially empty

    # Note: insert, search, build_from_list, inorder_traversal, and find_min 
    # are implemented in individual challenges below.
```

---

### 🧩 Challenge 1: Insert Value into BST

#### ❓ Problem

Implement `insert(self, value)` in class `BinarySearchTree` to add a new integer into the BST, preserving the BST property.

#### 📜 Description

* You have the `Node` class (holds `value`, `left`, `right`) and `BinarySearchTree` with attribute `root`.
* Implement `insert(self, value)` so that:

  1. If `self.root` is `None`, create `Node(value)` and set it as `self.root`.
  2. Otherwise, call a helper `_insert(node, value)` starting at `self.root`.
* `_insert(node, value)` must:

  * If `value < node.value` and `node.left` is `None`, assign `node.left = Node(value)`.
  * If `value < node.value` and `node.left` exists, recurse into `_insert(node.left, value)`.
  * If `value >= node.value` and `node.right` is `None`, assign `node.right = Node(value)`.
  * If `value >= node.value` and `node.right` exists, recurse into `_insert(node.right, value)`.
* **Do not modify** the class signature.

#### 🧪 5 Tests to Pass

1. **Insert into empty**:

   ```python
   bst = BinarySearchTree()
   bst.insert(10)
   # bst.root.value == 10
   ```
2. **Left child**:

   ```python
   bst = BinarySearchTree()
   bst.insert(10)
   bst.insert(5)
   # bst.root.left.value == 5
   ```
3. **Right child**:

   ```python
   bst = BinarySearchTree()
   bst.insert(10)
   bst.insert(15)
   # bst.root.right.value == 15
   ```
4. **Deep insert**:

   ```python
   bst = BinarySearchTree()
   for v in [10, 5, 15, 3, 7]:
       bst.insert(v)
   # bst.root.left.left.value == 3 and bst.root.left.right.value == 7
   ```
5. **Duplicates to right**:

   ```python
   bst = BinarySearchTree()
   bst.insert(10)
   bst.insert(10)
   # bst.root.right.value == 10
   ```

#### 🧩 Base Code

```python
class Node:
    """🌱 Node for Binary Search Tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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
* Use recursion in `_insert` to traverse until you find a `None` child.

#### 🧠 Motivation

Insertion shapes the BST structure, which determines search performance. Mastering this underpins many search-related algorithms.

---

### 🧩 Challenge 2: Search Value in BST

#### ❓ Problem

Implement `search(self, value)` in class `BinarySearchTree` to return `True` if the integer `value` exists in the tree, otherwise return `False`.

#### 📜 Description

* Use the `Node` and `BinarySearchTree` constructor from Common Code.
* This challenge’s base code **already includes** a fully implemented `insert` and `_insert` so you can build the tree. Focus **only** on writing the `search` and `_search` methods.
* `search(self, value)` should:

  1. If `self.root` is `None`, return `False`.
  2. Otherwise, call `_search(self.root, value)` and return its result.
* `_search(node, value)` must:

  * If `node is None`, return `False`.
  * If `node.value == value`, return `True`.
  * If `value < node.value`, return `_search(node.left, value)`.
  * Otherwise, return `_search(node.right, value)`.

#### 🧪 5 Tests to Pass

1. **Empty tree**:

   ```python
   bst = BinarySearchTree()
   # bst.search(5) should return False
   ```
2. **Root exists**:

   ```python
   bst = BinarySearchTree()
   bst.insert(10)
   # bst.search(10) should return True
   ```
3. **Left subtree**:

   ```python
   bst = BinarySearchTree()
   for v in [10, 5, 3]:
       bst.insert(v)
   # bst.search(3) should return True
   ```
4. **Right subtree**:

   ```python
   bst = BinarySearchTree()
   for v in [10, 5, 15, 20]:
       bst.insert(v)
   # bst.search(20) should return True
   ```
5. **Not found**:

   ```python
   bst = BinarySearchTree()
   for v in [10, 5, 15]:
       bst.insert(v)
   # bst.search(7) should return False
   ```

#### 🧩 Base Code

```python
class Node:
    """🌱 Node for Binary Search Tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """🌳 BST with working insert and incomplete search."""
    def __init__(self):
        self.root = None  # 📭 Initially empty

    def insert(self, value):
        """🧩 Insert a value into the BST (already implemented)."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        """🔄 Recursive helper for insert (already implemented)."""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

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
    print("👈 Test 3:", bst.search(3) == True)
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
* Compare `value` with `node.value` and recurse left or right accordingly.
* Return immediately when found.

#### 🧠 Motivation

Searching leverages BST structure to achieve **O(log n)** on average, which is foundational for fast lookups and dictionary-like data.

---

### 🧩 Challenge 3: Build BST from List of Values

#### ❓ Problem

Implement `build_from_list(self, values)` in `BinarySearchTree` to insert multiple integers in sequence.

#### 📜 Description

* Use `Node` and `BinarySearchTree` constructor from Common Code.
* This challenge’s base code **already includes** a fully implemented `insert` and `_insert` so you can focus **only** on writing `build_from_list`.
* `build_from_list(self, values)` should:

  1. Take `values`, a Python list of integers.
  2. For each integer in `values`, call `self.insert(val)`.
  3. After completion, `self.root` represents the BST containing all inserted values.
  4. Duplicates should go to the right (via `insert` logic).

#### 🧪 5 Tests to Pass

1. **Empty list**:

   ```python
   bst = BinarySearchTree()
   bst.build_from_list([])
   # bst.root is None
   ```
2. **Single element**:

   ```python
   bst = BinarySearchTree()
   bst.build_from_list([5])
   # bst.root.value == 5
   ```
3. **Multiple insert**:

   ```python
   bst = BinarySearchTree()
   bst.build_from_list([10, 5, 15])
   # bst.root.left.value == 5 and bst.root.right.value == 15
   ```
4. **Duplicates**:

   ```python
   bst = BinarySearchTree()
   bst.build_from_list([10, 10, 10])
   # root.value == 10, root.right.value == 10, root.right.right.value == 10
   ```
5. **Unsorted order** (use `inorder_traversal` from Challenge 4):

   ```python
   bst = BinarySearchTree()
   bst.build_from_list([7, 3, 11, 1, 5])
   ordered = []
   inorder_traversal(bst.root, ordered)
   # ordered == [1, 3, 5, 7, 11]
   ```

#### 🧩 Base Code

```python
class Node:
    """🌱 Node for Binary Search Tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """🌳 BST with working insert and incomplete build_from_list."""
    def __init__(self):
        self.root = None  # 📭 Initially empty

    def insert(self, value):
        """🧩 Insert a value into the BST (already implemented)."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        """🔄 Recursive helper for insert (already implemented)."""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def build_from_list(self, values):
        """📦 Build BST from a list of integer values."""
        # Your solution here 🛠️
        pass

# Reuse inorder_traversal from Challenge 4 for test 5:
def inorder_traversal(node, result_list):
    if node is None:
        return
    inorder_traversal(node.left, result_list)
    result_list.append(node.value)
    inorder_traversal(node.right, result_list)

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

* Simply loop over `values` and call `insert()` for each element.
* Reuse the already implemented `insert` method—do **not** reimplement insertion logic here.

#### 🧠 Motivation

Bulk-building from a list is practical when initializing a BST from a dataset (e.g., reading keys from a file).

---

### 🧩 Challenge 4: Inorder Traversal of BST

#### ❓ Problem

Implement the function `inorder_traversal(node, result_list)` to produce a sorted list of BST values.

#### 📜 Description

* Given `node` (root of a BST) and an empty list `result_list`, perform an **in-order traversal**:

  1. If `node is None`, return immediately.
  2. Recurse on `node.left`, appending values to `result_list`.
  3. Append `node.value` to `result_list`.
  4. Recurse on `node.right`.
* After the call, `result_list` must contain the BST keys in **ascending order**.
* You may use `insert` and `build_from_list` from earlier challenges to set up trees for testing.

#### 🧪 5 Tests to Pass

1. **Empty tree**:

   ```python
   result = []
   inorder_traversal(None, result)
   # result == []
   ```
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
* Ensure you append **after** the left subtree and **before** traversing the right subtree.

#### 🧠 Motivation

In-order traversal of a BST yields a **sorted** sequence—crucial for printing keys in order or validating that a tree is a valid BST.

---

### 🧩 Challenge 5: Find Minimum Value in BST

#### ❓ Problem

Implement `find_min(self)` in class `BinarySearchTree` that returns the **minimum** integer value stored in the BST, or `None` if the tree is empty.

#### 📜 Description

* In a BST, the leftmost node holds the minimum value.
* Starting at `self.root`, traverse left pointers until you reach a node with `left is None`.
* If `self.root` is `None`, return `None`.
* Otherwise, return the `value` of the leftmost node.
* You may use `insert` and `build_from_list` from earlier challenges to set up test trees.

#### 🧪 5 Tests to Pass

1. **Empty tree**:

   ```python
   bst = BinarySearchTree()
   # bst.find_min() should return None
   ```
2. **Single node**:

   ```python
   bst = BinarySearchTree()
   bst.insert(5)
   # bst.find_min() == 5
   ```
3. **Right-skewed**:

   ```python
   bst = BinarySearchTree()
   for v in [5, 10, 15]:
       bst.insert(v)
   # bst.find_min() == 5
   ```
4. **Left-skewed**:

   ```python
   bst = BinarySearchTree()
   for v in [5, 4, 3]:
       bst.insert(v)
   # bst.find_min() == 3
   ```
5. **Mixed**:

   ```python
   bst = BinarySearchTree()
   for v in [10, 5, 15, 2, 7]:
       bst.insert(v)
   # bst.find_min() == 2
   ```

#### 🧩 Base Code

```python
class Node:
    """🌱 Node for Binary Search Tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """🌳 BST with working insert and incomplete find_min."""
    def __init__(self):
        self.root = None  # 📭 Initially empty

    def insert(self, value):
        """🧩 Insert a value into the BST (already implemented)."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        """🔄 Recursive helper for insert (already implemented)."""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

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
* Otherwise, iterate:

  ```python
  current = self.root
  while current.left:
      current = current.left
  return current.value
  ```

#### 🧠 Motivation

Finding the minimum is often the first step in deletion algorithms and in-range queries. It highlights the BST’s structural advantage.

---

💡 *Created with AI support by Elliot Garamendi 👨‍💻*
🤖 *Assisted by ChatGPT – Your creative teaching co-pilot 🚀*

## o4 Advanced Binary Trees (AVL Insert/Delete, Rotations) 🧩🔁

In this section, you will implement core AVL tree operations: node structure, height calculation, balance factor, rotations, insertion with rebalancing, and deletion with rebalancing. Below, the **Common Code** provides only the `AVLNode` class and the `AVLTree` constructor; each challenge includes the dependent methods fully implemented except for the one you must complete. Only **one** challenge will be shown to the student at random, so focus **solely** on the empty method in that challenge.

---

### Common Code (Shared by All Challenges in o4)

```python
class AVLNode:
    """🌱 Node for AVL Tree (stores key, child pointers, and height)."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """🔄 AVL Tree skeleton; methods implemented in individual challenges."""
    def __init__(self):
        self.root = None  # 📭 Initially empty

    # Note: get_height, get_balance, rotations, insert, delete, etc.
    # are implemented in individual challenges below.
```

---

### 🧩 Challenge 1: Define AVL Node Structure

#### ✅ Title

🌱 AVLNode Initialization

#### ❓ Problem

Create a class `AVLNode` that stores an integer `key`, left/right child pointers, and a `height` attribute initialized to 1.

#### 📜 Description

* Implement `__init__(self, key)` so that:

  1. `self.key = key`
  2. `self.left = None`
  3. `self.right = None`
  4. `self.height = 1`
* Do **not** modify the class signature or add extra methods.

#### 🧪 5 Tests to Pass

1. Creating `node = AVLNode(10)` → `node.key == 10`.
2. `node.left is None`.
3. `node.right is None`.
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

* Assign each attribute (`key`, `left`, `right`, `height`) directly inside `__init__`.
* A new node is a leaf, so its `height` should start at 1.

#### 🧠 Motivation

Every AVL node must track its subtree height to detect imbalances. A correct node structure is the foundation of rotations and rebalancing.

---

### 🧩 Challenge 2: Height Utility & Balance Factor

#### ✅ Title

📏 Height and ⚖️ Balance Factor

#### ❓ Problem

Inside `AVLTree`, implement two methods:

1. `get_height(self, node)` – returns the `height` of an `AVLNode` or `0` if `node is None`.
2. `get_balance(self, node)` – returns `get_height(node.left) - get_height(node.right)`, or `0` if `node is None`.

#### 📜 Description

* Both methods belong to `class AVLTree`.
* Do **not** modify their signatures.
* If `node is None`, `get_height` returns `0`, and `get_balance` returns `0`.
* Otherwise, return the correct integer.

#### 🧪 5 Tests to Pass

1. `get_height(None) == 0`.
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
    def __init__(self):
        self.root = None

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

* In `get_height`, check `if node is None: return 0`; otherwise return `node.height`.
* In `get_balance`, if `node is None`, return `0`; else compute `get_height(node.left) - get_height(node.right)`.

#### 🧠 Motivation

Accurate height and balance-factor detection is crucial for deciding when rotations are needed, ensuring the tree remains O(log n).

---

### 🧩 Challenge 3: Perform Rotations (Left & Right)

#### ✅ Title

🔄 LeftRotate & 🔃 RightRotate

#### ❓ Problem

Inside `AVLTree`, implement two methods:

* `left_rotate(self, z)` – performs a left rotation on node `z` (RR case), returns the new root.
* `right_rotate(self, z)` – performs a right rotation on node `z` (LL case), returns the new root.

#### 📜 Description

* Both methods belong to `class AVLTree`.
* Use `get_height(...)` to update node heights after rotation.
* **Left Rotate** (RR case):

  1. Let `y = z.right` and `T2 = y.left`.
  2. Update pointers:

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
* **Right Rotate** (LL case) is symmetric:

  1. Let `y = z.left` and `T3 = y.right`.
  2. Update pointers:

     ```python
     y.right = z
     z.left = T3
     ```
  3. Update heights similarly.
  4. Return `y`.

#### 🧪 5 Tests to Pass

1. **Left Rotate Simple**

   ```python
   tree = AVLTree()
   z = AVLNode(10)
   z.right = AVLNode(20); z.right.height = 1
   z.height = 2
   new_root = tree.left_rotate(z)
   # new_root.key == 20, new_root.left.key == 10, new_root.left.right is None
   ```
2. **Right Rotate Simple**

   ```python
   tree = AVLTree()
   z = AVLNode(20)
   z.left = AVLNode(10); z.left.height = 1
   z.height = 2
   new_root = tree.right_rotate(z)
   # new_root.key == 10, new_root.right.key == 20, new_root.right.left is None
   ```
3. **Update Heights Left**

   ```python
   tree = AVLTree()
   z = AVLNode(30)
   z.right = AVLNode(40); z.right.height = 1
   z.height = 2
   new_root = tree.left_rotate(z)
   # new_root.height == 2 and new_root.left.height == 1
   ```
4. **Update Heights Right**

   ```python
   tree = AVLTree()
   z = AVLNode(30)
   z.left = AVLNode(20); z.left.height = 1
   z.height = 2
   new_root = tree.right_rotate(z)
   # new_root.height == 2 and new_root.right.height == 1
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
    def __init__(self):
        self.root = None

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
  3. `y.left = z; z.right = T2`
  4. Update `z.height` then `y.height`.
  5. Return `y`.
* For **right\_rotate**, swap left/right roles:

  1. `y = z.left`
  2. `T3 = y.right`
  3. `y.right = z; z.left = T3`
  4. Update heights similarly.
  5. Return `y`.

#### 🧠 Motivation

Rotations correct imbalances in O(1) time, ensuring inserts and deletes remain O(log n). Understanding rotations is key to keeping the AVL property.

---

### 🧩 Challenge 4: Insert with Rebalancing

#### ✅ Title

➕ AVL Insert with Rebalance

#### ❓ Problem

Inside `AVLTree`, implement a method `insert(self, node, key)` that:

1. Performs a normal BST insertion in the subtree rooted at `node`.
2. Updates `node.height`.
3. Computes `balance = self.get_balance(node)`.
4. Applies one of the four rotation cases (LL, RR, LR, RL) if `balance` goes out of `[-1,1]`.
5. Returns the (possibly new) subtree root.

#### 📜 Description

* Signature: `def insert(self, node, key) -> AVLNode`.
* If `node is None`, return `AVLNode(key)`.
* Recurse:

  ```python
  if key < node.key:
      node.left = self.insert(node.left, key)
  else:
      node.right = self.insert(node.right, key)
  ```
* After recursion, update:

  ```python
  node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
  balance = self.get_balance(node)
  ```
* **LL**: `if balance > 1 and key < node.left.key: return self.right_rotate(node)`
* **RR**: `if balance < -1 and key > node.right.key: return self.left_rotate(node)`
* **LR**:

  ```python
  if balance > 1 and key > node.left.key:
      node.left = self.left_rotate(node.left)
      return self.right_rotate(node)
  ```
* **RL**:

  ```python
  if balance < -1 and key < node.right.key:
      node.right = self.right_rotate(node.right)
      return self.left_rotate(node)
  ```
* Otherwise `return node`.

#### 🧪 5 Tests to Pass

1. **Simple Insert**

   ```python
   tree = AVLTree()
   root = tree.insert(None, 10)
   # root.key == 10 and root.height == 1
   ```
2. **LL Case**

   ```python
   tree = AVLTree()
   root = None
   for k in [30, 20, 10]:
       root = tree.insert(root, k)
   # root.key == 20, root.left.key == 10, root.right.key == 30
   ```
3. **RR Case**

   ```python
   tree = AVLTree()
   root = None
   for k in [10, 20, 30]:
       root = tree.insert(root, k)
   # root.key == 20, root.left.key == 10, root.right.key == 30
   ```
4. **LR Case**

   ```python
   tree = AVLTree()
   root = None
   for k in [30, 10, 20]:
       root = tree.insert(root, k)
   # root.key == 20, root.left.key == 10, root.right.key == 30
   ```
5. **RL Case**

   ```python
   tree = AVLTree()
   root = None
   for k in [10, 30, 20]:
       root = tree.insert(root, k)
   # root.key == 20, root.left.key == 10, root.right.key == 30
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
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return 0 if not node else node.height

    def get_balance(self, node):
        return 0 if not node else self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        """🔄 Left rotate (RR case)."""
        # Assume implemented in Challenge 3
        pass

    def right_rotate(self, z):
        """🔃 Right rotate (LL case)."""
        # Assume implemented in Challenge 3
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

1. **BST Insert**: If `node is None`, return `AVLNode(key)`.
2. **Recurse**: Compare `key` vs. `node.key` and insert into left or right subtree.
3. **Update Height**:

   ```python
   node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
   ```
4. **Compute Balance**:

   ```python
   balance = self.get_balance(node)
   ```
5. **Rotate if Needed**:

   * **LL**: `balance > 1 and key < node.left.key` → `return self.right_rotate(node)`
   * **RR**: `balance < -1 and key > node.right.key` → `return self.left_rotate(node)`
   * **LR**:

     ```python
     if balance > 1 and key > node.left.key:
         node.left = self.left_rotate(node.left)
         return self.right_rotate(node)
     ```
   * **RL**:

     ```python
     if balance < -1 and key < node.right.key:
         node.right = self.right_rotate(node.right)
         return self.left_rotate(node)
     ```
6. Return `node` if no rotation is needed.

#### 🧠 Motivation

Balanced insertion keeps the tree height within O(log n), guaranteeing efficient lookups and updates. Mastering these cases prevents degeneration into a linear list.

---

### 🧩 Challenge 5: Delete with Rebalancing

#### ✅ Title

➖ AVL Delete with Rebalance

#### ❓ Problem

Inside `AVLTree`, implement `delete(self, node, key)` that:

1. Performs a standard BST deletion of `key` under subtree `node`.
2. If the deleted node has two children, replace its `key` with the in-order successor’s key (`min_value_node(node.right)`).
3. Updates `node.height`.
4. Computes `balance = self.get_balance(node)`.
5. Rebalances via the four rotation cases (LL, LR, RR, RL) if `balance` goes out of `[-1,1]`.
6. Returns the (possibly new) subtree root.

#### 📜 Description

* Signature: `def delete(self, node, key) -> AVLNode`.
* If `node is None`, return `None`.
* Recurse:

  ```python
  if key < node.key:
      node.left = self.delete(node.left, key)
  elif key > node.key:
      node.right = self.delete(node.right, key)
  else:
      # Found node to delete
      if not node.left:
          return node.right
      elif not node.right:
          return node.left
      else:
          temp = self.min_value_node(node.right)
          node.key = temp.key
          node.right = self.delete(node.right, temp.key)
  ```
* After deletion adjustments, update:

  ```python
  node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
  balance = self.get_balance(node)
  ```
* **Left-heavy** (`balance > 1`):

  * If `self.get_balance(node.left) >= 0`: **LL** → `return self.right_rotate(node)`
  * Else (**LR**):

    ```python
    node.left = self.left_rotate(node.left)
    return self.right_rotate(node)
    ```
* **Right-heavy** (`balance < -1`):

  * If `self.get_balance(node.right) <= 0`: **RR** → `return self.left_rotate(node)`
  * Else (**RL**):

    ```python
    node.right = self.right_rotate(node.right)
    return self.left_rotate(node)
    ```
* Otherwise `return node`.

#### 🧪 5 Tests to Pass

1. **Delete Leaf**

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
   # result == [20, 30]
   ```
2. **Delete Node with One Child**

   ```python
   tree = AVLTree()
   root = None
   for k in [20, 10, 30, 5]:
       root = tree.insert(root, k)
   root = tree.delete(root, 10)
   result = []
   inorder(root, result)
   # result == [5, 20, 30]
   ```
3. **Delete Node with Two Children**

   ```python
   tree = AVLTree()
   root = None
   for k in [20, 10, 30, 5, 15]:
       root = tree.insert(root, k)
   root = tree.delete(root, 10)
   result = []
   inorder(root, result)
   # result == [5, 15, 20, 30]
   ```
4. **Rebalance After Deletion (LL)**

   ```python
   tree = AVLTree()
   root = None
   for k in [30, 20, 10, 5]:
       root = tree.insert(root, k)
   root = tree.delete(root, 5)
   result = []
   inorder(root, result)
   # result == [10, 20, 30]
   ```
5. **Rebalance After Deletion (RR)**

   ```python
   tree = AVLTree()
   root = None
   for k in [10, 20, 30, 40]:
       root = tree.insert(root, k)
   root = tree.delete(root, 10)
   result = []
   inorder(root, result)
   # result == [20, 30, 40]
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
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return 0 if not node else node.height

    def get_balance(self, node):
        return 0 if not node else self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        """🔄 Left rotation (RR case)."""
        # Assume implemented in Challenge 3
        pass

    def right_rotate(self, z):
        """🔃 Right rotation (LL case)."""
        # Assume implemented in Challenge 3
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

* Reuse `min_value_node(...)`, `get_height(...)`, `get_balance(...)`, and rotation methods from previous challenges.
* After removing or replacing a node, immediately update:

  ```python
  node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
  balance = self.get_balance(node)
  ```
* Apply **exactly** the same rotation cases as in `insert` (LL, LR, RR, RL).

#### 🧠 Motivation

Deletion plus rebalancing preserves AVL’s O(log n) performance, ensuring that even after removals the tree remains height-balanced. This is vital for consistently fast search, insert, and delete operations.

---

💡 *Created with AI support by Elliot Garamendi 👨‍💻*
🤖 *Assisted by ChatGPT – Your creative teaching co-pilot 🚀*
