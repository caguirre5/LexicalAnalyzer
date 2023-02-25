def infix_to_postfix(infix):
    precedence = {'*': 3, '+': 3, '?': 3, '.': 2, '|': 1}
    postfix = []
    stack = []

    for char in infix:
        if char in list(precedence.keys()):
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[char]:
                postfix.append(stack.pop())
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            postfix.append(char)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)


def input_transform(exp):
    # Agregar concatenación implícita
    exp = exp.strip()
    result = []
    for i in range(len(exp)):
        result.append(exp[i])
        if i + 1 < len(exp):
            if (exp[i] != '(' and exp[i] != '|' and exp[i + 1] != ')' and exp[i + 1] != '|' and exp[i + 1] != '*' and exp[i + 1] != '+' and exp[i + 1] != '?'):
                result.append('.')
    return ''.join(result)
