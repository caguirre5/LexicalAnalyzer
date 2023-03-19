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


class SubsetConstruction:
    def __init__(self, DFA):
        self.DFA = DFA
        self.Gs = [DFA.end]
        self.G2 = DFA.states
        self.G2.remove(DFA.end)
        self.Gs.append(self.G2)

    def minimization(self):
        while True:
            for Subset in self.Gs:
                for symbol in self.DFA.alphabet:
                    for state in Subset:
                        for transition in state.transitions:
                            if transition[0] == symbol:
                                pass
