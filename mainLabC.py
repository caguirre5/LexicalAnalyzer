import tools.textHandler as textHandler
import dataStructures.expressionTree as expressionTree
from algorithms.thompsonNFA import ThompsonNFA
from tools.drawAutomaton import getNFA, getDFA
from tools.drawTree import buildGraph
from algorithms.subsetDFA import SubsetConstruction
from tools.simulacion import simulate_afd, simulate_afn
from algorithms.directDFA import construct_afd
from algorithms.minimize import minimize_afd


# Definir las constantes para los tokens
WS = "WS"
ID = "ID"
PLUS = "PLUS"
TIMES = "TIMES"
LPAREN = "LPAREN"
RPAREN = "RPAREN"

precedence = {'*': 3, '+': 3, '?': 3, '.': 2, '|': 1}
# Definir una función para analizar cada token


def analizar_token(token):
    if token == "ws":
        return WS
    elif token == "id":
        return ID
    elif token == "+":
        return PLUS
    elif token == "*":
        return TIMES
    elif token == "(":
        return LPAREN
    elif token == ")":
        return RPAREN
    else:
        return None


def char_set(arr):
    pass


def genString(start, end):
    i = start
    string = chr(i)
    while i < end:
        i = i + 1
        if i == 91:
            i = 97
        string += '|'+chr(i)
    return string


def generate_regex(token, productions):
    production = productions[token]

    # Check if the production is a terminal (i.e. doesn't reference other tokens)
    if not any([t in production for t in productions.keys()]):
        return production

    # Replace each referenced token with its corresponding regex
    for t in productions.keys():
        if t in production:
            regex = generate_regex(t, productions)
            production = production.replace(t, regex)

    # If the token is 'ws', add a '+' at the end to indicate 1 or more occurrences
    if token == "ws":
        production += "+"

    print('production -> ', production)

    return f"({production})"


# Abrir el archivo de especificación de tokens
with open("./yalexFiles/slr-3.yal") as File:
    # Definir una lista para almacenar las líneas relevantes
    lineas_relevantes = []
    tokens = {}

    # Leer el archivo línea por línea
    for line in File:
        if line[0:3] == 'let':
            line = line[3:]
            pos = line.find('=')
            tokens[line[:pos].strip()] = line[pos+1:].strip()

    # # Manejo de tokens
    # for key in tokens.keys():
    #     # Si es un token de espacios
    #     if tokens[key] == "[' ''\\t''\\n']":
    #         tokens[key] = "' '|'\\t'|'\\n'"
    #     # Si es un token alfabetico
    #     elif tokens[key] == "['A'-'Z''a'-'z']":
    #         tokens[key] = genString(65, 122)
    #     # Si es un token numerico
    #     elif tokens[key] == "['0'-'9']" or tokens[key] == '["0123456789"]':
    #         tokens[key] = genString(48, 57)

    # for key, value in tokens.items():
    #     print(key, ":", value)
    #     token = ''
    #     temp = []
    #     for i, char in enumerate(value):
    #         if char in tokens.keys():
    #             pass
    #         else:
    #             token += char

    print(generate_regex('id', tokens))

    # if textHandler.is_valid_regex(regex):
    #     postfix, alphabet = textHandler.infix_to_postfix(regex)
    #     tree = ExpressionTree.buildTreeExpression(postfix)

    #     buildGraph(tree).view()
