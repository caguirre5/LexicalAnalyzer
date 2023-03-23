def simulate_afn(afn, string):
    current_states = set([afn.start])
    for symbol in string:
        next_states = set()
        for state in current_states:
            for transition in state.transitions:
                if transition[0] == symbol:
                    next_states.add(transition[1])
            next_states |= epsilon_closure(state)
        current_states = next_states
    for state in current_states:
        if state == afn.end:
            return True
    return False


def epsilon_closure(state):
    closure = set()
    stack = [state]
    while stack:
        current_state = stack.pop()
        closure.add(current_state)
        for transition in current_state.transitions:
            if transition[0] == 'eps' and transition[1] not in closure:
                stack.append(transition[1])
    return closure


def simulate_afd(afd, input_string):
    current_state = afd.start
    for symbol in input_string:
        found_transition = False
        for transition_symbol, next_state in current_state.transitions:
            if symbol == transition_symbol:
                current_state = next_state
                found_transition = True
                break
        if not found_transition:
            return False
    return current_state in afd.end


def move(state, symbol):  # Debe regresar un estado
    for transition in state.transitions:
        if transition[0] == symbol:
            state = transition[1]
        else:
            state = None
    return state
