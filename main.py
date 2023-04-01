import textHandler
import ExpressionTree

import networkx as nx
import matplotlib.pyplot as plt

from afn import ThompsonNFA
from drawAutomaton import getNFA, getDFA
from subsetDFA import SubsetConstruction
from simulacion import simulate_afd, simulate_afn
from directAFD import construct_afd
from minimize import minimize_afd


def agregar_nodos_y_aristas(raiz, nivel, G):
    G.add_node(raiz.value, level=nivel)
    if raiz.left is not None:
        G.add_edge(raiz.value, raiz.left.value)
        agregar_nodos_y_aristas(raiz.left, nivel + 1, G)
    if raiz.right is not None:
        G.add_edge(raiz.value, raiz.right.value)
        agregar_nodos_y_aristas(raiz.right, nivel + 1, G)


while True:
    infix = input("Ingrese una expresion regular: ")
    w = input("Ingrese una cadena a evaluar: ")
    # "(a|b)*a(a|b)(a|b)"
    if textHandler.is_valid_regex(infix):
        postfix, alphabet = textHandler.infix_to_postfix(infix)
        tree = ExpressionTree.buildTreeExpression(postfix)

        # Crear un objeto del grafo
        G = nx.DiGraph()

        # Agregar la raiz del árbol
        G.add_node(tree.value, level=0)

        # Agregar el resto de los nodos y aristas
        agregar_nodos_y_aristas(tree, 1, G)

        # Obtener los niveles de los nodos
        niveles = [G.nodes[n]['level'] for n in G.nodes()]

        # Graficar el árbol
        pos = nx.layout.hierarchy_layout(G, root=tree.value)
        nx.draw_networkx(G, pos, with_labels=True, node_size=500,
                         node_color='lightblue', font_size=12, font_weight='bold', levels=niveles)
        plt.axis('off')
        plt.show()

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
