class Token:
    def __init__(self, value):
        self.value = value

class Node:
    def __init__(self, value):
        self.isRoot = False
        self.left = None
        self.right = None
        self.value = value
        self.position = None
