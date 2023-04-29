class State:
    def __init__(self, label, subset=None):
        self.label = label
        self.transitions = {}


class AFD:
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
        self.states = []


class DirectAFD:
    def __init__(self, expression_tree):
        self.current_label = 0

    def firstpos(self, node, first):
        if node.label == 'ε':
            return
        if node.label in ['*', '+', '?']:
            self.firstpos(node.transitions[0], first)
        elif node.label == '.':
            if node.transitions[0].nullable:
                self.firstpos(node.transitions[0], first)
                self.firstpos(node.transitions[1], first)
            else:
                self.firstpos(node.transitions[0], first)
        else:
            first.add(node)

    def lastpos(self, node, last):
        if node.label == 'ε':
            return
        if node.label in ['*', '+', '?']:
            self.lastpos(node.transitions[0], last)
        elif node.label == '.':
            if node.transitions[1].nullable:
                self.lastpos(node.transitions[0], last)
                self.lastpos(node.transitions[1], last)
            else:
                self.lastpos(node.transitions[1], last)
        else:
            last.add(node)

    def followpos(self, node):
        if node.label in ['*', '+', '?']:
            for pos in node.lastpos:
                pos.followpos |= node.firstpos
        elif node.label == '.':
            for pos in node.transitions[0].lastpos:
                pos.followpos |= node.transitions[1].firstpos

    def get_label(self):
        self.current_label += 1
        return str(self.current_label)

    def construction(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            node.position = self.get_label()
        self.construction(node.left)
        self.construction(node.right)

    def construct_afd(self, postfix):
        stack = []
        for c in postfix:
            if c == '*':
                state = State(c)
                state.transitions[0] = stack.pop()
                state.firstpos = state.transitions[0].firstpos.copy()
                state.lastpos = state.transitions[0].lastpos.copy()
                for pos in state.lastpos:
                    pos.followpos |= state.firstpos
                stack.append(state)
            elif c == '+':
                state = State(c)
                state.transitions[0] = stack.pop()
                state.firstpos = state.transitions[0].firstpos.copy()
                state.lastpos = state.transitions[0].lastpos.copy()
                for pos in state.lastpos:
                    pos.followpos |= state.firstpos
                stack.append(state)
            elif c == '?':
                state = State(c)
                state.transitions[0] = stack.pop()
                state.transitions[1] = State('ε')
                state.firstpos = state.transitions[0].firstpos.copy()
                state.firstpos |= state.transitions[1].firstpos.copy()
                state.lastpos = state.transitions[0].lastpos.copy()
                state.lastpos |= state.transitions[1].lastpos.copy()
                for pos in state.lastpos:
                    pos.followpos |= state.firstpos
                stack.append(state)
            elif c == '.':
                state = State(c)
                state.transitions[1] = stack.pop()
                state.transitions[0] = stack.pop()
                state.firstpos = state.transitions[0].firstpos.copy()
                if state.transitions[0].nullable:
                    state.firstpos |= state.transitions[1].firstpos.copy()
                state.lastpos = state.transitions[1].lastpos.copy()
                if state.transitions[1].nullable:
                    state.lastpos |= state.transitions[0].lastpos.copy()
                for pos in state.transitions[0].lastpos:
                    pos.followpos |= state.transitions[1].firstpos
                stack.append(state)
            elif c == '|':
                state = State(c)
