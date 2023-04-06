import tools.textHandler as textHandler
import dataStructures.expressionTree as expressionTree
from algorithms.thompsonNFA import ThompsonNFA
from tools.drawAutomaton import getNFA, getDFA
from tools.drawTree import buildGraph
from algorithms.subsetDFA import SubsetConstruction
from tools.simulacion import simulate_afd, simulate_afn
from algorithms.directDFA import construct_afd
from algorithms.minimize import minimize_afd

while True:
    infix = input("Ingrese una expresion regular: ")
    w = input("Ingrese una cadena a evaluar: ")
    # "(a|b)*a(a|b)(a|b)"
    if textHandler.is_valid_regex(infix):
        postfix, alphabet = textHandler.infix_to_postfix(infix)
        tree = expressionTree.buildTreeExpression(postfix)

        buildGraph(tree).view()

        NFA = ThompsonNFA(tree, alphabet).getAFN()
        DFA = SubsetConstruction(NFA).getDFA()
        getNFA(NFA)
        getDFA(DFA)

        # if simulate_afn(NFA, w):
        #     print('>>> La cadena {} es aceptada por el AFN'.format(w))
        # else:
        #     print('>>> La cadena {} no es aceptada por el AFN'.format(w))

        if simulate_afd(DFA, w):
            print('>>> La cadena {} es aceptada por el AFD'.format(w))
        else:
            print('>>> La cadena {} no es aceptada por el AFD'.format(w))

#         print(DFA.alphabet)
# # ------------------------------------------------
        try:
            AFDdirect = construct_afd(postfix)
            getDFA((AFDdirect))
        except:
            print('Ocurrió un error en la construccion directa del AFD')

#         try:
#             Minimization = minimize_afd(DFA)
#         except:
#             print('Ocurrió un error en la minimizacion del AFD')
