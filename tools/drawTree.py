from graphviz import Digraph


def buildGraph(node, name):
    graph = Digraph('TREE', filename=name, format='png')
    graph.node(str(id(node)), str(node.value))

    if node.left:
        graph.edge(str(id(node)), str(id(node.left)), label='')
        graph.subgraph(buildGraph(node.left, name))

    if node.right:
        graph.edge(str(id(node)), str(id(node.right)), label='')
        graph.subgraph(buildGraph(node.right, name))

    return graph
