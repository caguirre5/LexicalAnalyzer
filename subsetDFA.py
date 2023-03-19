class State:
    def __init__(self, label, subset=None):
        self.marked = False
        self.label = label
        self.transitions = []
        self.subset = subset


class Subset:
    def __init__(self, subset):
        self.subset = subset
        self.transitions = []


class AFD:
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
        self.states = []

# Recibe un automata no determinista


class SubsetConstruction:
    def __init__(self, DFA):
        # dstates -> Lista de subconjuntos -> Lista de estados
        self.dstates = []
        # Subconjunto -> Lista de estados
        self.markedStates = []
        self.states = []
        self.alphabet = DFA.alphabet
        self.current_label = 0
        self.automaton = DFA
        self.DFA = []
        self.construction(DFA)

    def get_label(self):
        self.current_label += 1
        return str(self.current_label)

    def construction(self, DFA):
        stack = []
        marked = []
        newState_temp = State(self.get_label(), self.e_closure([DFA.start]))
        self.dstates.append(newState_temp)
        stack.append(newState_temp)
        # ---------------------------------------------------------A
        while self.dstates:
            state = self.dstates.pop(0)
            for symbol in self.alphabet:
                # U -> lista de estados
                U = self.e_closure(self.move(state.subset, symbol))
                # Verifica si el subset encontrado ya existe en dstates
                if U:  # Si el subset no es vacio
                    state_validation = self.equal_arrays(stack, U)
                    if state_validation:  # Si el subet ya existe
                        # Se agrega una transicion hacia ese estado
                        state.transitions.append((symbol, state_validation))
                    else:  # si no
                        # se crea un nuevo estado con el subset encontrado
                        newState = State(self.get_label(), U)
                        self.dstates.append(newState)  # se agrega a dstates
                        stack.append(newState)  # se agrega a stack general
                        state.transitions.append((symbol, newState))
            state.marked = True
            marked.append(state)
        # print('Nuevos estados: ', self.dstates)
        # print('Elementos del primer subconjunto: ',
        #       self.dstates[0].subset)
        # print('Transiciones: ', self.dstates[0].transitions)
        self.create_afd(stack)

    def create_afd(self, markedStates):
        start = markedStates.pop(0)
        end = []
        # se crea un conjunto de estados del automata y se agrega el estado inicial
        states = [start]
        while markedStates:
            state = markedStates.pop(0)
            # Verificar si es final
            if self.automaton.end in state.subset:
                # Si es, se agrega al conjunto de estados de aceptacion del automata
                end.append(state)
            else:
                # Si no, se agrega al conjunto de estados del automata
                states.append(state)
        states.extend(end)
        automaton = AFD(start, end)
        automaton.states.extend(states)
        self.DFA.append(automaton)

    def e_closure(self, subset):
        states = []
        states.extend(subset)
        while subset:
            element = subset.pop()
            for transition in element.transitions:
                if transition[0] == 'ε' and transition[1] not in states:
                    states.append(transition[1])
                    subset.append(transition[1])
        return states

    def printSubset(self, subset):
        string = '['
        for state in subset:
            string = string + '({})'.format(state.label)
        string = string + ']'
        return string

    def move(self, subset, symbol):
        states = []
        for element in subset:
            for transition in element.transitions:
                if transition[0] == symbol:
                    states.append(transition[1])
        return states

    def getLabels(self, states):
        labels = []
        for state in states:
            labels.append(state.label)
        return labels

    def equal_arrays(self, collection, arr):
        result = None
        new_collection = []
        for state in collection:
            new_collection.append(state.subset)

        lst_set = set(arr)
        for elem in collection:
            element = set(elem.subset)
            if element == lst_set:
                return elem
        return None

    def getDFA(self):
        DFA = self.DFA.pop()
        return DFA
