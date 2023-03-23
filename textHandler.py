class ErrorMessage(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return f"MiExcepcion: {self.mensaje}"


def infix_to_postfix(exp):
    infix = input_transform(exp)
    precedence = {'*': 3, '+': 3, '?': 3, '.': 2, '|': 1}
    postfix = []
    stack = []
    alphabet = []

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
            if char not in alphabet and char != 'ε':
                alphabet.append(char)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix), alphabet


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


def is_valid_regex(regex):
    stack = []
    valid_symbols = ['(', ')', '*', '+', '?', '|']

    for i, c in enumerate(regex):
        if c not in valid_symbols and not c.isalnum():
            print('-INVALID EXPRESSION-\n>>> {}th character <<{}>> is not a valid symbol and also not an alphanumeric character'.format(i+1, c))
            return False
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0 or stack.pop() != '(':
                print(
                    '-INVALID EXPRESSION-\n>>> No opening parenthesis found for a closing parenthesis.')
                return False
    if len(stack) != 0:
        print('-INVALID EXPRESSION-\n>>>The parentheses are not balanced.')
        return False
    for i, c in enumerate(regex):
        if c == '|' and (i == 0 or i == len(regex) - 1 or regex[i-1] == '|' or regex[i+1] == '|' or regex[i-1] == '(' or regex[i+1] == ')' or regex[i-1] == '.' or regex[i+1] == '.'):
            print(
                '-INVALID EXPRESSION-\n>>> A " | " symbol has been found in an invalid position at {}th character.'.format(i+1))
            return False
        elif c == '*' and (i == 0 or regex[i-1] == '|' or regex[i-1] == '(' or regex[i-1] == '*' or regex[i-1] == '+' or regex[i-1] == '?' or regex[i-1] == '.'):
            print(
                '-INVALID EXPRESSION-\n>>> A " * " symbol has been found in an invalid position at {}th character.'.format(i+1))
            return False
        elif c == '+' and (i == 0 or regex[i-1] == '|' or regex[i-1] == '(' or regex[i-1] == '*' or regex[i-1] == '+' or regex[i-1] == '?' or regex[i-1] == '.'):
            print(
                '-INVALID EXPRESSION-\n>>> A " + " symbol has been found in an invalid position at {}th character.'.format(i+1))
            return False
        elif c == '?' and (i == 0 or regex[i-1] == '|' or regex[i-1] == '(' or regex[i-1] == '*' or regex[i-1] == '+' or regex[i-1] == '?' or regex[i-1] == '.'):
            print(
                '-INVALID EXPRESSION-\n>>> A " ? " symbol has been found in an invalid position at {}th character.'.format(i+1))
            return False
        # elif c == '.' and (i == 0 or i == len(regex) - 1 or regex[i-1] == '|' or regex[i+1] == '|' or regex[i-1] == '(' or regex[i+1] == ')' or regex[i-1] == '*' or regex[i-1] == '+' or regex[i-1] == '?' or regex[i+1] == '*' or regex[i+1] == '+' or regex[i+1] == '?'):
        #     print(
        #         '-INVALID EXPRESSION-\n>>> A " . " symbol has been found in an invalid position at {}th character.'.format(i+1))
        #     return False
    return True
