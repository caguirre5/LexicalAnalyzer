from node import Node


def buildTreeExpression(postfix):
    stack = []
    ops = ['*', '+', '|', '.']
    for token in postfix:
        if token not in ops:
            node = Node(token)
            stack.append(node)
        else:
            node = Node(token)
            node.right = stack.pop()
            if token == '*' or token == '+':
                left = None
            else:
                left = stack.pop()
            node.left = left
            stack.append(node)
        print('vamos por el token: ', token)
    return stack.pop()
