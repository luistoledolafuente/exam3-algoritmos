def infix_to_postfix(tokens):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2}
    out, stack = [], []
    for t in tokens:
        if t.isalnum():
            out.append(t)
        elif t == '(':
            stack.append(t)
        elif t == ')':
            while stack[-1] != '(': out.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and prec[stack[-1]] >= prec[t]:
                out.append(stack.pop())
            stack.append(t)
    while stack:
        out.append(stack.pop())
    return out

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