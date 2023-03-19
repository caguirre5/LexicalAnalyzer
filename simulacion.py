def simularAFD(cadena, AF):
    S = AF.start
    for i, char in enumerate(cadena):
        S = move(S, char)
        if S == None:
            print('>>> La cadena {} no es aceptada'.format(cadena))
            break
    # if S in AF.end:
    #     print('>>> La cadena {} es aceptada'.format(cadena))
    # elif S not in AF.end:
    #     print('>>> La cadena {} no es aceptada'.format(cadena))


def simularAFN(cadena, AF):
    S = AF.start
    for char in cadena:
        S = move(S, char)
    if S == AF.end:
        print('>>> La cadena {} es aceptada'.format(cadena))
    else:
        print('>>> La cadena {} no es aceptada'.format(cadena))


def move(state, symbol):  # Debe regresar un estado
    for transition in state.transitions:
        if transition[0] == symbol:
            state = transition[1]
        else:
            state = None
    return state
