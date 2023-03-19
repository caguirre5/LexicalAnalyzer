from collections import deque


class State:
    def __init__(self, label, subset=None):
        self.marked = False
        self.label = label
        self.transitions = []
        self.subset = subset


class AFD:
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
        self.states = []

# Recibe un automata no determinista


def minimize_afd(AFD):
    alphabet = AFD.alphabet
    G1 = AFD.end
    G2 = [elem for elem in AFD.states if elem not in AFD.end]

    P1 = [G1, G2]
    print('G1 ', P1[0])
    print('G2 ', P1[1])

    notcomplete = True
    counter = 1

    while notcomplete:
        counter += 1
        print(">>>>El nuevo P1", P1)
        new_group = []
        for Group in P1:
            print('Evaluamos el grupo ', Group)
            for symbol in alphabet:
                print('Evaluamos el simbolo ', symbol)
                transition_group = {}
                for state in Group:
                    print('Evaluamos el estado ', state.label)
                    transition_found = None
                    for transition in state.transitions:
                        if transition[0] == symbol:
                            transition_found = transition
                    if transition_found:
                        for group in P1:
                            if transition_found[1] in group:
                                transition_group[state] = (
                                    transition_found, P1.index(group))
                        print('Encontramos la transicion: ({}, {})'.format(
                            transition_found[0], transition_found[1].label))
                        print('### ')
                        # new_group.append(state)
                    # Group.remove(state)
                    # new_group.append(state)
                if len(transition_group) > 0:

                    groups = DictHandler(transition_group)
                    if len(groups) > 1:
                        new_group.extend(groups)

                # if len(new_group) > 0:
                #     temp.append(new_group)
                #     print('Grupo de transiciones para el simbolo {} con el grupo {}: {}'.format(
                #         symbol, Group, transition_group))
        if len(groups) > 1:
            pass


def DictHandler(diccionario):
    grouped_dict = {}

    for key, value in diccionario.items():
        if value[1] not in grouped_dict:
            grouped_dict[value[1]] = []
        grouped_dict[value[1]].append(key)

    grupos = []

    for key, value in diccionario.items():
        grupos.append(value)

    return grupos
