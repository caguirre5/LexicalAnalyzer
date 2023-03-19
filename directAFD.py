class State:
    def __init__(self, label, subset=None):
        self.label = label
        self.transitions = []
        self.subset = subset


class AFD:
    def __init__(self, start=None, end=None, states=None):
        self.start = start
        self.end = end
        self.states = states or []


def nullable(node):
    if node is None:
        return False
    elif node.value == 'eps':
        return True
    elif node.value == 'char':
        return False
    elif node.value == '|':
        return nullable(node.left) or nullable(node.right)
    elif node.value == '.':
        return nullable(node.left) and nullable(node.right)
    elif node.value == '*':
        return True
    elif node.value == '+':
        return nullable(node.left) and node.right.value == '*'
    elif node.value == '?':
        return True


def firstpos(node):
    if node is None:
        return set()
    elif node.value == 'eps':
        return set()
    elif node.value == 'char':
        return set([node])
    elif node.value == '|':
        left = firstpos(node.left)
        right = firstpos(node.right)
        if left is None:
            left = set()
        if right is None:
            right = set()
        return left.union(right)
    elif node.value == '.':
        left = firstpos(node.left)
        right = firstpos(node.right)
        if left is None or right is None:
            return set()
        elif nullable(node.left):
            return left.union(right)
        else:
            return left
    elif node.value == '*':
        return firstpos(node.left)
    elif node.value == '+':
        return firstpos(node.left)
    elif node.value == '?':
        return firstpos(node.left)


def lastpos(node):
    if node is None:
        return set()
    elif node.value == 'eps':
        return set()
    elif node.value == 'char':
        return set([node])
    elif node.value == '|':
        return lastpos(node.left).union(lastpos(node.right))
    elif node.value == '.':
        if nullable(node.right):
            return lastpos(node.left).union(lastpos(node.right))
        else:
            return lastpos(node.right)
    elif node.value == '*':
        return lastpos(node.left)
    elif node.value == '+':
        return lastpos(node.left)
    elif node.value == '?':
        return lastpos(node.left)


def followpos(node):
    if node is None:
        return {}
    elif node.value == 'char':
        return {}
    elif node.value == '.':
        if nullable(node.left):
            return {n: lastpos(node.right) for n in firstpos(node.left)}
        else:
            return {n: firstpos(node.right) for n in lastpos(node.left)}
    elif node.value == '*':
        return {n: firstpos(node) for n in lastpos(node)}
    elif node.value == '+':
        return {n: firstpos(node) for n in lastpos(node)}
    elif node.value == '|':
        return {n: firstpos(node.left).union(firstpos(node.right)) for n in lastpos(node)}


def construct_afd(root):
    start = State(sorted(list(firstpos(root))), subset=None)
    states = [start]
    i = 0
    while i < len(states):
        state = states[i]
        for c in root.charset:
            next_subset = set()
            for n in state.label:
                next_subset = next_subset.union(followpos(n).get(c, set()))
            if len(next_subset) == 0:
                continue
            next_subset = sorted(list(next_subset))
            next_state = None
            for s in states:
                if s.subset == next_subset:
                    next_state = s
                    break
            if next_state is None:
                next_state = State(next_subset)
                states.append(next_state)
            state.transitions.append((c, next_state))
        i += 1

    end = State(sorted(list(lastpos(root))), subset=None)
    for s in states:
        if set(s.label).intersection(end.label):
            s.is_end = True

    return AFD(start=start, end=end, states=states)
