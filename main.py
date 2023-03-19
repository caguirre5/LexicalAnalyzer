import textHandler
import ExpressionTree
from afn import ThompsonNFA
from drawAutomaton import getNFA, getDFA
from subsetDFA import SubsetConstruction
from simulacion import simularAFD, simularAFN

while True:
    infix = input("Ingrese una expresion regular: ")
    w = input("Ingrese una cadena a evaluar en AFD: ")
    # "(a|b)*a(a|b)(a|b)"
    if textHandler.is_valid_regex(infix):
        postfix, alphabet = textHandler.infix_to_postfix(infix)
        tree = ExpressionTree.buildTreeExpression(postfix)

        NFA = ThompsonNFA(tree, alphabet).getAFN()
        getNFA(NFA)
        DFA = SubsetConstruction(NFA).getDFA()
        getDFA(DFA)

        simularAFD(w, DFA)
