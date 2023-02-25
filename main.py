import node
import toPostfix
import ExpressionTree
import afn
from afn import ThompsonNFA

infix = "(a|b)*a(a|b)(a|b)"  # Aun hay que averiguar
infix = toPostfix.input_transform(infix)
postfix = toPostfix.infix_to_postfix(infix)

print(postfix)
tree = ExpressionTree.buildTreeExpression(postfix)

nfa = ThompsonNFA(tree)
AFN = nfa.getAFN()
