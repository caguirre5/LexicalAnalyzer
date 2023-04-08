from dataStructures.node import Token

class yalReader:
    def __init__(self, path=None):
        self.ops = ['(', ')','+']
        self.tokensDict = {}
        self.regex = ''
        
        with open(path) as file:
            self.tokensDict = self.initializeTokens(file)

            self.printTokens(self.tokensDict)

            self.tokensDict = self.getTokensTransformation(self.tokensDict)

            self.printTokens(self.tokensDict)

            self.regex = self.concatExpressions(self.tokensDict)

    def initializeTokens(self, file):
        tokens = {}

        # Leer el archivo línea por línea
        for line in file:
            if line[0:3] == 'let':
                line = line[3:]
                pos = line.find('=')
                tokens[line[:pos].strip()] = line[pos+1:].strip()
        return tokens


    def generate_regex(self, token, productions):
        production = productions[token]
        # print('production -> ',production)
        # Check if the production is a terminal (i.e. doesn't reference other tokens)
        if not any([t in production for t in productions.keys()]):
            new_value = self.charSetConstruction(production)
            if new_value:
                production = new_value
            new_value = self.delimConstruction(production)
            if new_value:
                production = new_value
            return f"{production}"

        # Replace each referenced token with its corresponding regex
        for t in productions.keys():
            #Encontramos el char que sigue despues del token evaluado
            pos = production.find(t) + len(t)
            # Si el token esta en la produccion y el siguiente caracter es un operador
            if t in production and production[pos] in self.ops:
                #reemplazamos el token en la produccion por su valor terminal
                regex = self.generate_regex(t, productions)
                production = production.replace(t, regex)
                
        return f"{production}"
    
    def getTokensTransformation(self, tokens):
        transformedTokens = {}
        for token in tokens.keys():
            transformedTokens[token] = self.generate_regex(token, tokens)

        return transformedTokens
    
    def getCharSet(self, start, end):
        i = start
        lista = [chr(i)]
        while i < end:
            i = i + 1
            if i == 91:
                i = 97
            lista.append('|')
            lista.append(chr(i))

        return lista

    
    def delimConstruction(self, line):
        symbolSet = []
        symbol = ''
        validating = False
        if '["\s\t\n"]' in line:
            symbolSet.extend(["\s",'|',9,'|',10])
        else:
            for i, char in enumerate(line):
                if validating:
                    if char == "'":
                        if symbol == ' ':
                            symbol= "0"
                        symbolSet.extend([symbol,'|'])
                        validating = False
                        symbol=''
                    else:
                        symbol += char
                elif char == "'":
                    validating = True

        if len(symbolSet)>0:
            symbolSet.pop()
            symbolSet.insert(0,'(')
            symbolSet.append(')')
            return symbolSet


    def charSetConstruction(self, line):
        symbolSet = []
        comilla_found = False
        for i, char in enumerate(line):
            if char == '-' and line[i-2]!="'" and line[i+2]!="'":
                # Se encuentra un charset y se construye usando su codigo ascii
                #                             start            end
                symbolSet.extend(self.getCharSet(ord(line[i-2]), ord(line[i+2])))
                symbolSet.append('|')
            if char == '"' :
                comilla_found = not comilla_found
            elif comilla_found:
                symbolSet.append(char) 
                symbolSet.append('|')
        if len(symbolSet)>0:
            symbolSet.pop()
            symbolSet.insert(0,'(')
            symbolSet.append(')')
            return symbolSet


    def concatExpressions(self, tokens):
        meg_expression = ''
        for key in tokens.keys():
            meg_expression += tokens[key] + '|'
        return meg_expression[:-1]
    
    def concatExpressions2(self, tokens):
        meg_expression = []
        for key in tokens.keys():
            sub_expression = []
            for elem in tokens[key]:
                meg_expression.append()
                # tokens[key] + '|'
        return meg_expression[:-1]

    def printTokens(self, tokens):
        # print(tokens)
        print('-------------------------------------')
        for key,value in tokens.items():
            print('{} -> {}'.format(key, value))
        print('-------------------------------------')

    def getResults(self):
        return self.tokensDict, self.regex
