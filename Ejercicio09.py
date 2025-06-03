def infix_to_postfix(tokens):
    """
    🔁 Convert a list of infix tokens to postfix notation.
    """
    precedence = {'+':1, '-':1, '*':2, '/':2}
    stack = []
    output = []

    for token in tokens:
        if token.isalnum():  # operand (número o variable)
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            # sacar hasta encontrar '('
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # quitar '('
        else:
            # operador
            while stack and stack[-1] != '(' and precedence.get(stack[-1],0) >= precedence.get(token,0):
                output.append(stack.pop())
            stack.append(token)
    # vaciar pila
    while stack:
        output.append(stack.pop())

    return output


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
