import tools.textHandler as textHandler
import dataStructures.expressionTree as expressionTree
from tools.yalexReader2 import yalReader

yal = yalReader('./yalexFiles/slr-2.yal')

tokens, regex = yal.getResults()

print('-------------------------------------\n\t\tTOKENS\n-------------------------------------')
for key,value in tokens.items():
    print('{} -> {}'.format(key, value))
print('-------------------------------------')

print('\nLa expresion regular resultante es: \n',regex)




# if textHandler.is_valid_regex(regex):
postfix, alphabet = textHandler.infix_to_postfix2(regex)
print('POSTFIX-> \n',postfix)
#     tree = ExpressionTree.buildTreeExpression(postfix)

#     buildGraph(tree).view()
