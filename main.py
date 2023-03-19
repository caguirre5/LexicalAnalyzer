import textHandler
import ExpressionTree
from afn import ThompsonNFA
from drawAutomaton import getNFA, getDFA
from subsetDFA import SubsetConstruction
from simulacion import simulate_afd, simulate_afn
from directAFD import construct_afd

while True:
    infix = input("Ingrese una expresion regular: ")
    w = input("Ingrese una cadena a evaluar: ")
    # "(a|b)*a(a|b)(a|b)"
    if textHandler.is_valid_regex(infix):
        postfix, alphabet = textHandler.infix_to_postfix(infix)
        tree = ExpressionTree.buildTreeExpression(postfix)

        NFA = ThompsonNFA(tree, alphabet).getAFN()
        getNFA(NFA)
        DFA = SubsetConstruction(NFA).getDFA()
        getDFA(DFA)

        if simulate_afn(NFA, w):
            print('>>> La cadena {} es aceptada por el AFN'.format(w))
        else:
            print('>>> La cadena {} no es aceptada por el AFN'.format(w))

        if simulate_afd(DFA, w):
            print('>>> La cadena {} es aceptada por el AFD'.format(w))
        else:
            print('>>> La cadena {} no es aceptada por el AFD'.format(w))


# ------------------------------------------------
    AFDdirect = construct_afd(tree)
