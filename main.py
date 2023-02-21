import node
import toPostfix
import ExpressionTree

infix = 'a.b.(a|b)*.b'  # Aun hay que averiguar
postfix = toPostfix.infix_to_postfix(infix)

print(ExpressionTree.buildTreeExpression(postfix))
