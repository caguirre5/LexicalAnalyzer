import tools.textHandler as textHandler
import dataStructures.expressionTree as expressionTree
from tools.yalexReader import yalReader
from tools.drawTree import buildGraph

regexs = []

for i in range(1, 5):
    yal = yalReader('./yalexFiles/slr-{}.yal'.format(i))

    tokens, regex = yal.getResults()
    regexs.append(regex)

    print('-------------------------------------\n\t\tTOKENS\n-------------------------------------')
    for key,value in tokens.items():
        print('{} -> {}'.format(key, value))
    print('-------------------------------------')

    print('\nLa expresion regular del archivo slr-{}.yal es: \n'.format(i),regex)


    # if textHandler.is_valid_regex(regex):
    postfix, alphabet = textHandler.infix_to_postfix2(regex)
    tree = expressionTree.buildTreeExpression(postfix)

    name = './ImageResults/expressionTree_file{}'.format(i)
    buildGraph(tree, name).view()

print(regexs)

# Abrir el archivo de texto en modo escritura
with open('./ImageResults/regularExpresions', 'w') as archivo:
    # Escribir cada elemento de la lista en una línea separada
    archivo.writelines([elemento + '\n' for elemento in regexs])