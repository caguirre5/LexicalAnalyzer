import textHandler
import ExpressionTree
from afn import ThompsonNFA

while True:
    infix = input("Ingrese una expresion regular: ")
    # "(a|b)*a(a|b)(a|b)"
    if textHandler.is_valid_regex(infix):
        postfix = textHandler.infix_to_postfix(infix)
        tree = ExpressionTree.buildTreeExpression(postfix)

        ThompsonNFA(tree).getAFN()
