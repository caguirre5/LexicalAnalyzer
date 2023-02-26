from graphviz import Digraph


class State:
    def __init__(self, label):
        self.label = label
        self.transitions = []


class AFN:
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
        self.states = [self.start, self.end]


class ThompsonNFA:
    def __init__(self, expression_tree):
        self.states = []
        self.current_label = 0
        self.stack = []
        self.create_afn(expression_tree)

    def get_label(self):
        self.current_label += 1
        return str(self.current_label)

    def create_afn(self, node):
        root = node
        if root is None:
            return

        if root.left is None and root.right is None:
            start_state = State(self.get_label())
            end_state = State(self.get_label())
            start_state.transitions.append((root.value, end_state))
            self.states.append(start_state)
            self.states.append(end_state)
            self.stack.append(AFN(start_state, end_state))
        else:
            self.create_afn(root.left)
            self.create_afn(root.right)

            if root.value == '.':
                right_afn = self.stack.pop()
                left_afn = self.stack.pop()

                start_state = left_afn.start
                end_state = right_afn.end

                left_afn.end.transitions.append(('ε', right_afn.start))
                self.stack.append(AFN(start_state, end_state))

            elif root.value == '|':
                right_afn = self.stack.pop()
                left_afn = self.stack.pop()

                start_state = State(self.get_label())
                end_state = State(self.get_label())

                start_state.transitions.extend([
                    ('ε', left_afn.start), ('ε', right_afn.start)])
                left_afn.end.transitions.append(('ε', end_state))
                right_afn.end.transitions.append(('ε', end_state))

                self.states.extend([start_state, end_state])

                self.stack.append(AFN(start_state, end_state))

            elif root.value == '*':
                afn = self.stack.pop()
                start_state = State(self.get_label())
                end_state = State(self.get_label())

                start_state.transitions.extend(
                    [('ε', afn.start), ('ε', end_state)])
                afn.end.transitions.extend(
                    [('ε', end_state), ('ε', afn.start)])

                self.states.extend([start_state, end_state])

                self.stack.append(AFN(start_state, end_state))

            elif root.value == '+':
                afn = self.stack.pop()
                start_state = State(self.get_label())
                end_state = State(self.get_label())

                start_state.transitions.append(('ε', afn.start))
                afn.end.transitions.extend(
                    [('ε', end_state), ('ε', afn.start)])

                self.states.extend([start_state, end_state])

                self.stack.append(AFN(start_state, end_state))

            elif root.value == '?':
                afn = self.stack.pop()
                start_state = State(self.get_label())
                end_state = State(self.get_label())

                start_state.transitions.extend(
                    [('ε', afn.start), ('ε', end_state)])
                afn.end.transitions.append(('ε', end_state))

                self.states.extend([start_state, end_state])

                self.stack.append(AFN(start_state, end_state))

        return

    def getAFN(self):
        g = Digraph('NFA', filename='nfa', format='png')
        g.attr(rankdir='LR')

        AFN = self.stack.pop()
        for state in self.states:
            if state == AFN.end:
                g.node(str(state.label), shape='doublecircle', rank='same')
            elif state == AFN.start:
                g.node(str(state.label), shape='circle',
                       style='filled', fillcolor='green', rank='same')
            else:
                g.node(str(state.label), shape='circle')
            # ('edge label', 'end')
            for tran in state.transitions:
                g.edge(str(state.label), str(
                    tran[1].label), label=str(tran[0]))
        g.view()
        return AFN
