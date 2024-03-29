class yalReader:
    def __init__(self, path=None):
        self.ops = ['(', ')','+']
        self.tokensDict = {}
        self.regex = ''
        
        with open(path) as file:
            self.tokensDict = self.initializeTokens(file)
  
        self.tokensDict = self.getTokensTransformation(self.tokensDict)
        self.regex = self.concatExpressions(self.tokensDict)

    def initializeTokens(self, file):
        tokens = {}

        # Leer el archivo línea por línea
        for line in file:
            if line[0:3] == 'let':
                line = line[3:]
                pos = line.find('=')
                value = line[pos+1:].strip()
                value = self.otherConstruction(value)
                tokens[line[:pos].strip()] = value
        return tokens


    def generate_regex(self, token, productions):
        production = productions[token]
        # Chequeamos si la produccion es un terminal, si lo es, solo retornamos la misma produccion
        if not any([t in production for t in productions.keys()]):
            new_value = self.charSetConstruction(production)
            if new_value:
                production = new_value
            new_value = self.delimConstruction(production)
            if new_value:
                production = new_value
            return f"{production}"

        # Reemplazamos cada simbolo no terminal con su respectivo terminal
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
        string = chr(i)
        while i < end:
            i = i + 1
            if i == 91:
                i = 97
            string += '|'+chr(i)
        return string
    
    def otherConstruction(self, line):
        line = line.replace('["\\s\\t\\n"]', "(^|@|&)")
        line = line.replace("['+''-']", "(>|<)")
        line = line.replace("'E'", "E")
        line = line.replace("(_)", "(~)")
        line = line.replace(".", "#")
        return line

    
    def delimConstruction(self, line):
        symbolSet = ''
        symbol = ''
        validating = False
        comilla_found = False
        if '["\\s\\t\\n"]' in line:
            line = line.replace('["\\s\\t\\n"]', '&|@|$')
        for i, char in enumerate(line):
            if validating:
                if char == "'":
                    if symbol == ' ':
                        symbol='~'
                    elif symbol == '\\n':
                        symbol='$'
                    elif symbol == '\\t':
                        symbol='@'
                    symbolSet += symbol + '|'
                    symbol = ''
                    validating = False
                else:
                    symbol += char
                    # symbolSet = symbolSet + char
            elif char == "'":
                validating = True
            if char == '"' :
                comilla_found = not comilla_found
            elif comilla_found:
                symbolSet += f"{char}|"

        symbolSet=symbolSet[:-1]
        if len(symbolSet) > 0:
            return f"({symbolSet})"


    def charSetConstruction(self, line):
        symbolSet = ''
        comilla_found = False
        for i, char in enumerate(line):
            if char == '-' and line[i-2]!="'" and line[i+2]!="'":
                # Se encuentra un charset y se construye usando su codigo ascii
                #                             start            end
                symbolSet+=self.getCharSet(ord(line[i-2]), ord(line[i+2]))+'|'
            if char == '"' :
                comilla_found = not comilla_found
            elif comilla_found:
                symbolSet += f"{char}|"
        if len(symbolSet)>0:
            return f"({symbolSet[:-1]})"


    def concatExpressions(self, tokens):
        meg_expression = ''
        for key in tokens.keys():
            meg_expression += tokens[key] + '|'
        return meg_expression[:-1]

    def printTokens(self, tokens):
        # print(tokens)
        print('-------------------------------------')
        for key,value in tokens.items():
            print('{} -> {}'.format(key, value))
        print('-------------------------------------')

    def getResults(self):
        return self.tokensDict, self.regex
