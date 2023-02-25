from graphviz import Digraph


def dfs(node):
    if node:
        dfs(node.left)
        dfs(node.right)


g = Digraph('NFA', filename='nfa.gv', format='png')
g.attr(rankdir='LR')

g.node('0', shape='invtriangle', dir='back')
g.node('1', shape='circle')
g.node('2', shape='circle')
# ...node [shape=doublecircle style=filled fillcolor=white]
g.edge('0', '1', label='a')
g.edge('1', '2', label='b')
g.edge('1', '2', label='b')
# ...
g.view()
