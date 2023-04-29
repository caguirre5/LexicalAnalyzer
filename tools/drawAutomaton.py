from graphviz import Digraph


def getNFA(NFA):
    g = Digraph('NFA', filename='./ImageResults/NFA', format='png')
    g.attr(rankdir='LR')
    for state in NFA.states:
        if state == NFA.end:
            g.node(str(state.label), shape='doublecircle', rank='same')
        elif state == NFA.start:
            g.node(str(state.label), shape='circle',
                   style='filled', fillcolor='green', rank='same')
        else:
            g.node(str(state.label), shape='circle')
        # ('edge label', 'end')
        for tran in state.transitions:
            g.edge(str(state.label), str(
                tran[1].label), label=str(tran[0]))
    g.view()
    return


def getDFA(DFA):
    g = Digraph('DFA', filename='./ImageResults/DFA', format='png')
    g.attr(rankdir='LR')
    for state in DFA.states:
        g.node(str(state.label), shape='circle')
        if state == DFA.start:
            g.node(str(state.label),
                   style='filled', fillcolor='green', rank='same')
        if state in DFA.end:
            g.node(str(state.label), shape='doublecircle', rank='same')
        # ('edge label', 'end')
        for tran in state.transitions:
            g.edge(str(state.label), str(
                tran[1].label), label=str(tran[0]))
    g.view()
    return
