from graphviz import Digraph


def buildGraph(node):
    graph = Digraph('TREE', filename='tree', format='png')
    graph.node(str(id(node)), str(node.value))

    if node.left:
        graph.edge(str(id(node)), str(id(node.left)), label='')
        graph.subgraph(buildGraph(node.left))

    if node.right:
        graph.edge(str(id(node)), str(id(node.right)), label='')
        graph.subgraph(buildGraph(node.right))

    return graph
