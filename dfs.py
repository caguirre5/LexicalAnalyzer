
def dfs(node):
    if node is None:
        return

    print(node.value)
    dfs(node.left)
    dfs(node.right)
