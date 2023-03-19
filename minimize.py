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
        self.DFA = DFA
        self.G1 = DFA.end
        self.G2 = DFA.state
        self.G2.remove(DFA.end)
